#!/usr/bin/env python3
"""
Process archived memory exports into AI-ready, navigable chunks.

Design goals:
- Preserve original archive files in /memories unchanged.
- Never truncate source text.
- Process one root memory file at a time.
- Extract ZIP contents safely.
- Convert readable files into Markdown chunks plus JSONL metadata.
- Keep manifests so an AI architect can navigate by archive, source file, and chunk.

Generated output lives under:
  memories/processed/

This script is deterministic and safe to rerun. It rebuilds the generated folder.
"""

from __future__ import annotations

import base64
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
MEMORIES_DIR = ROOT / "memories"
OUTPUT_DIR = MEMORIES_DIR / "processed"
EXTRACTED_DIR = OUTPUT_DIR / "_extracted_raw"
CHUNKS_DIR = OUTPUT_DIR / "chunks"
INDEX_DIR = OUTPUT_DIR / "indexes"

MAX_CHARS = int(os.environ.get("MEMORY_CHUNK_MAX_CHARS", "12000"))
OVERLAP_CHARS = int(os.environ.get("MEMORY_CHUNK_OVERLAP_CHARS", "600"))

TEXT_EXTENSIONS = {
    ".txt", ".md", ".markdown", ".json", ".jsonl", ".csv", ".tsv",
    ".html", ".htm", ".xml", ".yaml", ".yml", ".js", ".ts", ".tsx",
    ".jsx", ".py", ".css", ".scss", ".sql", ".log", ".ini", ".toml",
    ".rst", ".rtf", ".svg"
}

BINARY_PREVIEW_BYTES = 96


@dataclass
class ChunkRecord:
    archive_id: str
    archive_filename: str
    source_path: str
    chunk_id: str
    chunk_index: int
    chunk_count_for_source: int
    output_path: str
    source_sha256: str
    chunk_sha256: str
    char_start: int
    char_end: int
    char_count: int
    format: str


@dataclass
class SourceRecord:
    archive_id: str
    archive_filename: str
    source_path: str
    extracted_path: str | None
    source_sha256: str
    byte_count: int
    detected_type: str
    chunk_count: int
    parse_status: str
    notes: str


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str, max_len: int = 96) -> str:
    value = value.replace("\\", "/")
    value = re.sub(r"[^A-Za-z0-9._/-]+", "-", value)
    value = value.strip("-._/")
    value = value.replace("/", "__")
    if not value:
        value = "item"
    return value[:max_len]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_extract_member(zip_file: zipfile.ZipFile, member: zipfile.ZipInfo, destination: Path) -> Path | None:
    # Ignore directories.
    if member.is_dir():
        return None
    raw_name = member.filename.replace("\\", "/")
    raw_name = raw_name.lstrip("/")
    parts = [p for p in raw_name.split("/") if p not in ("", ".", "..")]
    if not parts:
        return None
    safe_path = destination.joinpath(*parts).resolve()
    destination_resolved = destination.resolve()
    if destination_resolved not in safe_path.parents and safe_path != destination_resolved:
        raise ValueError(f"Unsafe ZIP path blocked: {member.filename}")
    safe_path.parent.mkdir(parents=True, exist_ok=True)
    with zip_file.open(member) as source, safe_path.open("wb") as target:
        shutil.copyfileobj(source, target)
    return safe_path


def detect_text(data: bytes, path: Path) -> tuple[bool, str]:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTENSIONS:
        return True, suffix.lstrip(".") or "text"
    if b"\x00" in data[:4096]:
        return False, "binary"
    try:
        data[:8192].decode("utf-8")
        return True, "text"
    except UnicodeDecodeError:
        try:
            data[:8192].decode("utf-16")
            return True, "utf16-text"
        except UnicodeDecodeError:
            return False, "binary"


def decode_text(data: bytes) -> str:
    for encoding in ("utf-8", "utf-8-sig", "utf-16", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    # Last resort; never drop bytes silently. Replacement characters mark undecodable spans.
    return data.decode("utf-8", errors="replace")


def normalize_json_text(text: str) -> str:
    try:
        parsed = json.loads(text)
    except Exception:
        return text
    return json.dumps(parsed, indent=2, ensure_ascii=False)


def normalize_csv_text(text: str, delimiter: str = ",") -> str:
    # Keep all cells but render as markdown-ish rows for AI readability.
    try:
        rows = list(csv.reader(text.splitlines(), delimiter=delimiter))
    except Exception:
        return text
    if not rows:
        return text
    rendered = []
    for row in rows:
        rendered.append(" | ".join(cell.strip() for cell in row))
    return "\n".join(rendered)


def prepare_ai_text(text: str, source_path: str) -> tuple[str, str]:
    suffix = Path(source_path).suffix.lower()
    if suffix == ".json":
        return normalize_json_text(text), "json"
    if suffix == ".jsonl":
        return text, "jsonl"
    if suffix == ".csv":
        return normalize_csv_text(text, ","), "csv"
    if suffix == ".tsv":
        return normalize_csv_text(text, "\t"), "tsv"
    if suffix in (".md", ".markdown"):
        return text, "markdown"
    if suffix in (".html", ".htm"):
        return text, "html"
    return text, "text"


def split_text(text: str, max_chars: int = MAX_CHARS, overlap: int = OVERLAP_CHARS) -> list[tuple[int, int, str]]:
    if len(text) <= max_chars:
        return [(0, len(text), text)]
    chunks: list[tuple[int, int, str]] = []
    start = 0
    length = len(text)
    while start < length:
        hard_end = min(start + max_chars, length)
        end = hard_end
        if hard_end < length:
            # Prefer section, paragraph, then line boundaries near the end.
            window_start = max(start + int(max_chars * 0.6), start)
            boundary_candidates = [
                text.rfind("\n## ", window_start, hard_end),
                text.rfind("\n\n", window_start, hard_end),
                text.rfind("\n", window_start, hard_end),
                text.rfind(". ", window_start, hard_end),
            ]
            best = max(boundary_candidates)
            if best > window_start:
                end = best + 1
        chunk = text[start:end]
        chunks.append((start, end, chunk))
        if end >= length:
            break
        start = max(0, end - overlap)
        if start >= end:
            start = end
    return chunks


def write_chunk(record_base: dict[str, Any], chunk_text: str, chunk_index: int, chunk_count: int, output_subdir: Path) -> ChunkRecord:
    chunk_id = f"{record_base['archive_id']}__{record_base['source_slug']}__chunk-{chunk_index:04d}"
    output_subdir.mkdir(parents=True, exist_ok=True)
    output_file = output_subdir / f"{chunk_id}.md"
    char_start, char_end = record_base["chunk_ranges"][chunk_index - 1]

    header = {
        "chunk_id": chunk_id,
        "archive_id": record_base["archive_id"],
        "archive_filename": record_base["archive_filename"],
        "source_path": record_base["source_path"],
        "chunk_index": chunk_index,
        "chunk_count_for_source": chunk_count,
        "char_start": char_start,
        "char_end": char_end,
        "source_sha256": record_base["source_sha256"],
        "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
    }

    output_file.write_text(
        "---\n"
        + json.dumps(header, indent=2, ensure_ascii=False)
        + "\n---\n\n"
        + chunk_text
        + ("\n" if not chunk_text.endswith("\n") else ""),
        encoding="utf-8"
    )

    return ChunkRecord(
        archive_id=record_base["archive_id"],
        archive_filename=record_base["archive_filename"],
        source_path=record_base["source_path"],
        chunk_id=chunk_id,
        chunk_index=chunk_index,
        chunk_count_for_source=chunk_count,
        output_path=str(output_file.relative_to(ROOT)),
        source_sha256=record_base["source_sha256"],
        chunk_sha256=sha256_bytes(chunk_text.encode("utf-8")),
        char_start=char_start,
        char_end=char_end,
        char_count=len(chunk_text),
        format=record_base["format"],
    )


def iter_root_memory_files() -> Iterable[Path]:
    if not MEMORIES_DIR.exists():
        return []
    ignored = {"processed"}
    files = []
    for path in sorted(MEMORIES_DIR.iterdir(), key=lambda p: p.name.lower()):
        if path.name in ignored or path.name.startswith("."):
            continue
        if path.is_file() and path.suffix.lower() in {".zip", ".json", ".md", ".txt"}:
            files.append(path)
    return files


def process_text_source(
    archive_id: str,
    archive_filename: str,
    source_path: str,
    data: bytes,
    extracted_path: Path | None,
    source_records: list[SourceRecord],
    chunk_records: list[ChunkRecord],
) -> None:
    source_sha = sha256_bytes(data)
    is_text, detected_type = detect_text(data, Path(source_path))
    if not is_text:
        preview = base64.b64encode(data[:BINARY_PREVIEW_BYTES]).decode("ascii")
        source_records.append(SourceRecord(
            archive_id=archive_id,
            archive_filename=archive_filename,
            source_path=source_path,
            extracted_path=str(extracted_path.relative_to(ROOT)) if extracted_path else None,
            source_sha256=source_sha,
            byte_count=len(data),
            detected_type=detected_type,
            chunk_count=0,
            parse_status="binary_not_chunked",
            notes=f"Binary file preserved in original archive. First {BINARY_PREVIEW_BYTES} bytes base64 preview: {preview}",
        ))
        return

    text = decode_text(data)
    prepared, fmt = prepare_ai_text(text, source_path)
    chunks = split_text(prepared)
    source_slug = slugify(source_path)
    output_subdir = CHUNKS_DIR / archive_id
    chunk_ranges = [(start, end) for start, end, _ in chunks]
    base = {
        "archive_id": archive_id,
        "archive_filename": archive_filename,
        "source_path": source_path,
        "source_slug": source_slug,
        "source_sha256": source_sha,
        "format": fmt,
        "chunk_ranges": chunk_ranges,
    }
    for idx, (_, _, chunk_text) in enumerate(chunks, start=1):
        chunk_records.append(write_chunk(base, chunk_text, idx, len(chunks), output_subdir))

    source_records.append(SourceRecord(
        archive_id=archive_id,
        archive_filename=archive_filename,
        source_path=source_path,
        extracted_path=str(extracted_path.relative_to(ROOT)) if extracted_path else None,
        source_sha256=source_sha,
        byte_count=len(data),
        detected_type=fmt,
        chunk_count=len(chunks),
        parse_status="chunked",
        notes="Text converted into AI-ready Markdown chunks with no truncation.",
    ))


def process_zip(path: Path, source_records: list[SourceRecord], chunk_records: list[ChunkRecord]) -> dict[str, Any]:
    archive_id = slugify(path.stem)
    archive_out_dir = EXTRACTED_DIR / archive_id
    archive_out_dir.mkdir(parents=True, exist_ok=True)
    archive_sha = sha256_bytes(path.read_bytes())
    processed_members = 0

    with zipfile.ZipFile(path, "r") as zf:
        for member in sorted(zf.infolist(), key=lambda m: m.filename.lower()):
            if member.is_dir():
                continue
            extracted = safe_extract_member(zf, member, archive_out_dir)
            if extracted is None:
                continue
            data = extracted.read_bytes()
            process_text_source(
                archive_id=archive_id,
                archive_filename=path.name,
                source_path=member.filename,
                data=data,
                extracted_path=extracted,
                source_records=source_records,
                chunk_records=chunk_records,
            )
            processed_members += 1

    return {
        "archive_id": archive_id,
        "archive_filename": path.name,
        "archive_type": "zip",
        "archive_sha256": archive_sha,
        "processed_member_count": processed_members,
    }


def process_plain_file(path: Path, source_records: list[SourceRecord], chunk_records: list[ChunkRecord]) -> dict[str, Any]:
    archive_id = slugify(path.stem)
    data = path.read_bytes()
    process_text_source(
        archive_id=archive_id,
        archive_filename=path.name,
        source_path=path.name,
        data=data,
        extracted_path=None,
        source_records=source_records,
        chunk_records=chunk_records,
    )
    return {
        "archive_id": archive_id,
        "archive_filename": path.name,
        "archive_type": path.suffix.lower().lstrip(".") or "file",
        "archive_sha256": sha256_bytes(data),
        "processed_member_count": 1,
    }


def write_indexes(archives: list[dict[str, Any]], source_records: list[SourceRecord], chunk_records: list[ChunkRecord]) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    index = {
        "generated_at": now_iso(),
        "generator": "scripts/process-memories.py",
        "chunking": {
            "max_chars": MAX_CHARS,
            "overlap_chars": OVERLAP_CHARS,
            "no_truncation_policy": True,
        },
        "archives": archives,
        "source_count": len(source_records),
        "chunk_count": len(chunk_records),
        "output_roots": {
            "chunks": str(CHUNKS_DIR.relative_to(ROOT)),
            "indexes": str(INDEX_DIR.relative_to(ROOT)),
            "extracted_raw": str(EXTRACTED_DIR.relative_to(ROOT)),
        }
    }

    (OUTPUT_DIR / "README.md").write_text(
        "# Processed AI Memory\n\n"
        "Generated from files stored in `/memories`. Original ZIP and JSON files remain unchanged.\n\n"
        "## Folders\n"
        "- `chunks/`: AI-ready Markdown chunks split by archive and source file.\n"
        "- `indexes/`: JSON/JSONL navigation indexes for agents.\n"
        "- `_extracted_raw/`: safely extracted raw ZIP contents for audit/reference.\n\n"
        "## Rules\n"
        "- Generated files are rebuildable.\n"
        "- Source archives are the immutable memory evidence.\n"
        "- Chunk files include YAML-style JSON metadata headers.\n"
        "- Text is split with overlap and no truncation.\n",
        encoding="utf-8"
    )

    (INDEX_DIR / "archive-index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (INDEX_DIR / "sources.json").write_text(json.dumps([asdict(r) for r in source_records], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (INDEX_DIR / "chunks.json").write_text(json.dumps([asdict(r) for r in chunk_records], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with (INDEX_DIR / "chunks.ndjson").open("w", encoding="utf-8") as f:
        for record in chunk_records:
            f.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    # Human navigation map.
    by_archive: dict[str, list[ChunkRecord]] = {}
    for chunk in chunk_records:
        by_archive.setdefault(chunk.archive_id, []).append(chunk)

    lines = ["# AI Memory Navigation Map", "", f"Generated: {index['generated_at']}", ""]
    for archive in archives:
        archive_id = archive["archive_id"]
        lines.append(f"## {archive['archive_filename']}")
        lines.append(f"- Archive ID: `{archive_id}`")
        lines.append(f"- SHA-256: `{archive['archive_sha256']}`")
        lines.append(f"- Processed members: {archive['processed_member_count']}")
        archive_chunks = by_archive.get(archive_id, [])
        lines.append(f"- Chunk count: {len(archive_chunks)}")
        for chunk in archive_chunks[:25]:
            lines.append(f"  - `{chunk.output_path}` — source `{chunk.source_path}` chunk {chunk.chunk_index}/{chunk.chunk_count_for_source}")
        if len(archive_chunks) > 25:
            lines.append(f"  - ... {len(archive_chunks) - 25} more chunks listed in `indexes/chunks.json`")
        lines.append("")
    (INDEX_DIR / "NAVIGATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not MEMORIES_DIR.exists():
        print("No memories directory found.", file=sys.stderr)
        return 1

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    archives: list[dict[str, Any]] = []
    source_records: list[SourceRecord] = []
    chunk_records: list[ChunkRecord] = []

    for path in iter_root_memory_files():
        print(f"Processing {path.relative_to(ROOT)}")
        try:
            if path.suffix.lower() == ".zip":
                archives.append(process_zip(path, source_records, chunk_records))
            else:
                archives.append(process_plain_file(path, source_records, chunk_records))
        except zipfile.BadZipFile:
            data = path.read_bytes()
            archives.append({
                "archive_id": slugify(path.stem),
                "archive_filename": path.name,
                "archive_type": "invalid_zip",
                "archive_sha256": sha256_bytes(data),
                "processed_member_count": 0,
                "error": "BadZipFile",
            })
            source_records.append(SourceRecord(
                archive_id=slugify(path.stem),
                archive_filename=path.name,
                source_path=path.name,
                extracted_path=None,
                source_sha256=sha256_bytes(data),
                byte_count=len(data),
                detected_type="invalid_zip",
                chunk_count=0,
                parse_status="error",
                notes="ZIP could not be opened by Python zipfile.",
            ))

    write_indexes(archives, source_records, chunk_records)
    print(f"Processed {len(archives)} root memory files, {len(source_records)} sources, {len(chunk_records)} chunks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
