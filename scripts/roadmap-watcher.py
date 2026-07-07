#!/usr/bin/env python3
"""
Roadmap Watcher: AI agent that thinks like Aaron.

Reads memory digests, raw fallback context, and roadmap deep-context files;
extracts actionable claims; maps them to pillars; validates for public-safe
roadmap use; and proposes roadmap updates.

Key operating rules:
- Evidence-based: every proposal points back to a digest/context source.
- Linear: preserve the main path and move side quests later instead of losing them.
- Public-safe: do not promote private/contact/financial/travel details into public roadmap output.
- Practical: blockers and frontier should reflect the work that is actually active now.
- Deep-context aware: roadmap-deep-context files are directional source material and must be consulted before changing frontier, pillar priority, sequencing, or project boundaries. They are not published raw.
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEEP_CONTEXT_DIR = DATA_DIR / "roadmap-deep-context"

# The 8 Pillars - Aaron's operating tracks.
# Production Atlas is active because the July 2026 digests show current repository/research work.
PILLARS = {
    "pillar-1": {
        "title": "Deadhang Labor LLC",
        "track": "business_operations",
        "priority": "critical",
        "status": "active",
    },
    "pillar-2": {
        "title": "The Crew Blueprint",
        "track": "content_platform",
        "priority": "high",
        "status": "active",
    },
    "pillar-3": {
        "title": "Production Atlas",
        "track": "software_projects",
        "priority": "high",
        "status": "active",
    },
    "pillar-4": {
        "title": "Contractor Tools",
        "track": "software_projects",
        "priority": "high",
        "status": "active",
    },
    "pillar-5": {
        "title": "Land Acquisition",
        "track": "land_and_legacy",
        "priority": "medium",
        "status": "future",
    },
    "pillar-6": {
        "title": "Homestead Network / Homes for Hands",
        "track": "land_and_legacy",
        "priority": "low",
        "status": "future",
    },
    "pillar-7": {
        "title": "Personal Operations / Roadmap System",
        "track": "personal_admin",
        "priority": "critical",
        "status": "active",
    },
    "pillar-8": {
        "title": "Skills & Certifications",
        "track": "skills_progression",
        "priority": "high",
        "status": "active",
    },
}

STATUS_ALIASES = {
    "completed": "completed",
    "done": "completed",
    "shipped": "completed",
    "active": "active",
    "in progress": "active",
    "current": "active",
    "blocked": "blocked",
    "deferred": "moved_later",
    "moved_later": "moved_later",
    "moved later": "moved_later",
    "future": "moved_later",
}

PRIORITY_SCORES = {
    "critical": 10,
    "high": 7,
    "medium": 3,
    "low": 1,
}

PROJECT_TYPES = {"project", "active", "pivot", "pillar_baseline"}


class RoadmapWatcher:
    """Aaron's roadmap watcher - direct, evidence-linked, anti-sprawl, and deep-context aware."""

    def __init__(self):
        self.memory_sources: Dict[str, Dict[str, Any]] = {}
        self.deep_context_sources: List[Dict[str, Any]] = []
        self.claims: List[Dict[str, Any]] = []
        self.proposals: Dict[str, List[Dict[str, Any]]] = {
            "projects": [],
            "tasks": [],
            "completed": [],
            "moved_later": [],
            "blockers": [],
            "conflicts": [],
        }
        self.frontier: Optional[Dict[str, Any]] = None

    def normalize_status(self, raw: Optional[str], default: str = "active") -> str:
        if not raw:
            return default
        status_text = raw.strip().lower()
        for key, value in STATUS_ALIASES.items():
            if key in status_text:
                return value
        return default

    def load_memory_index(self) -> bool:
        """Load the memory index when present. Digest parsing still works without it."""
        index_file = ROOT / "memories" / "processed" / "indexes" / "sources.json"
        if not index_file.exists():
            print("⚠️  Memory index not found. Continuing with digest files.")
            return False

        try:
            with open(index_file, encoding="utf-8") as f:
                sources = json.load(f)

            relevant = [
                s
                for s in sources
                if any(
                    keyword in s.get("archive_id", "").lower()
                    for keyword in [
                        "chatgpt-export",
                        "claude-batch",
                        "kimi-batch",
                        "gemini",
                        "festival-atlas",
                        "perplexity",
                        "contentrepo",
                    ]
                )
            ]
            self.memory_sources = {s.get("source_path", str(i)): s for i, s in enumerate(relevant)}
            print(f"✓ Loaded {len(self.memory_sources)} memory sources")
            return True
        except Exception as exc:
            print(f"⚠️  Failed to load memory index: {exc}. Continuing with digest files.")
            return False

    def extract_section_text(self, content: str, heading: str) -> str:
        pattern = rf"##\s+{re.escape(heading)}\s*\n([\s\S]*?)(?=\n##\s+|\Z)"
        match = re.search(pattern, content, re.IGNORECASE)
        if not match:
            return ""
        return re.sub(r"\s+", " ", match.group(1)).strip()

    def infer_deep_context_pillars(self, content: str) -> List[str]:
        lowered = content.lower()
        pillars = []
        checks = {
            "pillar-1": ["deadhang", "labor llc", "field-to-homestead"],
            "pillar-2": ["crew blueprint", "technical education", "stagehand", "rigging", "av"],
            "pillar-3": ["production atlas", "resource infrastructure", "nomadic resource"],
            "pillar-4": ["contractor tools", "invoice", "laravel", "automation"],
            "pillar-5": ["land acquisition"],
            "pillar-6": ["homes for hands", "homestead", "sanctuary", "respite", "steward"],
            "pillar-7": ["roadmap", "time layer", "milestone", "personal operations", "anti-sprawl"],
            "pillar-8": ["skills", "certifications", "osha"],
        }
        for pillar, terms in checks.items():
            if any(term in lowered for term in terms):
                pillars.append(pillar)
        return pillars or ["pillar-7"]

    def load_deep_context_sources(self) -> List[Dict[str, Any]]:
        """
        Load roadmap-deep-context files as directional decision context.

        These files are intentionally not treated as raw public roadmap output.
        They influence frontier/priority/boundary decisions and should be cited
        whenever the watcher changes roadmap direction, sequencing, or scope.
        """
        sources: List[Dict[str, Any]] = []
        if not DEEP_CONTEXT_DIR.exists():
            print("ℹ️  No roadmap deep-context directory found.")
            self.deep_context_sources = []
            return sources

        for path in sorted(DEEP_CONTEXT_DIR.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            try:
                content = path.read_text(encoding="utf-8")
                title_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else path.stem
                core_meaning = self.extract_section_text(content, "Core Meaning")
                public_summary = self.extract_section_text(content, "Public-Safe Summary")
                sources.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "title": title,
                        "pillars": self.infer_deep_context_pillars(content),
                        "decision_use": "Consult before changing frontier, sequencing, pillar priority, project boundaries, or public-safe summaries.",
                        "summary": (public_summary or core_meaning)[:900],
                        "raw_publication_allowed": False,
                    }
                )
            except Exception as exc:
                print(f"  ⚠️  Could not load deep context {path.name}: {exc}")

        self.deep_context_sources = sources
        print(f"✓ Loaded {len(sources)} roadmap deep-context decision sources")
        return sources

    def make_claim(
        self,
        claim_type: str,
        description: str,
        pillar: str,
        source: str,
        status: str,
        evidence: Optional[str] = None,
        priority: Optional[str] = None,
    ) -> Dict[str, Any]:
        pillar = pillar if pillar in PILLARS else "pillar-7"
        return {
            "type": claim_type,
            "description": description.strip(),
            "pillar": pillar,
            "source": source,
            "status": status,
            "evidence": evidence or f"From {source} digest",
            "priority": priority or PILLARS[pillar]["priority"],
        }

    def split_numbered_blocks(self, section: str) -> List[str]:
        """Split markdown numbered-list sections into full multi-line item blocks."""
        blocks: List[str] = []
        current: List[str] = []
        for line in section.splitlines():
            if re.match(r"^\s*\d+\.\s+", line):
                if current:
                    blocks.append("\n".join(current).strip())
                current = [line]
            elif current:
                current.append(line)
        if current:
            blocks.append("\n".join(current).strip())
        return blocks

    def extract_claims_from_digest_files(self) -> List[Dict[str, Any]]:
        """Extract claims from data/raw-reports/*-digest.md."""
        claims: List[Dict[str, Any]] = []
        digest_dir = DATA_DIR / "raw-reports"

        if not digest_dir.exists():
            print("⚠️  No data/raw-reports directory found.")
            return claims

        for digest_file in sorted(digest_dir.glob("*-digest.md")):
            try:
                with open(digest_file, encoding="utf-8") as f:
                    content = f.read()

                source_name = digest_file.stem.replace("-digest", "")

                projects_section = re.search(
                    r"## Active Projects[\s\S]*?(?=\n## [^#]|\Z)",
                    content,
                    re.IGNORECASE,
                )
                if projects_section:
                    project_blocks = re.split(
                        r"\n(?=###\s+)",
                        projects_section.group(0),
                    )
                    for block in project_blocks:
                        header = re.search(r"^###\s+(.+?)\s*$", block, re.MULTILINE)
                        if not header:
                            continue
                        title = header.group(1).strip()
                        pillar_match = re.search(r"\*\*Pillar:\*\*\s*(pillar-\d+)", block)
                        pillar = pillar_match.group(1) if pillar_match else "pillar-7"
                        status_match = re.search(r"\*\*Status:\*\*\s*(.+?)(?:\n|$)", block)
                        status = self.normalize_status(status_match.group(1) if status_match else None)
                        claims.append(
                            self.make_claim(
                                "project",
                                title,
                                pillar,
                                source_name,
                                status,
                                evidence=f"From {source_name} digest",
                            )
                        )

                blockers_section = re.search(
                    r"## Blockers?[^\n]*[\s\S]*?(?=\n## [^#]|\Z)",
                    content,
                    re.IGNORECASE,
                )
                if blockers_section:
                    for block in self.split_numbered_blocks(blockers_section.group(0)):
                        title_match = re.search(r"\*\*(.+?)\*\*", block)
                        if not title_match:
                            continue
                        title = title_match.group(1).strip()
                        pillar_match = re.search(r"\*\*Pillar:\*\*\s*(pillar-\d+)", block)
                        pillar = pillar_match.group(1) if pillar_match else "pillar-7"
                        status_match = re.search(r"\*\*Status:\*\*\s*(.+?)(?:\n|$)", block)
                        status = self.normalize_status(status_match.group(1) if status_match else None, "blocked")
                        claims.append(
                            self.make_claim(
                                "blocker",
                                title,
                                pillar,
                                source_name,
                                status if status == "blocked" else "blocked",
                                evidence=f"From {source_name} digest",
                            )
                        )

            except Exception as exc:
                print(f"  ⚠️  Could not parse {digest_file.name}: {exc}")

        print(f"✓ Extracted {len(claims)} claims from digest files")
        return claims

    def extract_claims_from_context(self) -> bool:
        """Extract actionable claims and load deep-context decision sources."""
        print("🔍 Extracting claims from memories...")
        claims = self.extract_claims_from_digest_files()
        self.load_deep_context_sources()

        context_dir = (
            ROOT
            / "memories"
            / "processed"
            / "_extracted_raw"
            / "chatgpt-export-2026-07-05"
            / "aaron_bowman_context_export_md"
        )

        if context_dir.exists():
            claims.extend(self.extract_context_fallback_claims(context_dir))
        else:
            print("ℹ️  Extracted raw context not found. Digest claims are sufficient.")

        self.claims = self.dedupe_claims(claims)
        print(f"✓ Extracted {len(self.claims)} unique actionable claims")
        return True

    def extract_context_fallback_claims(self, context_dir: Path) -> List[Dict[str, Any]]:
        """Fallback extraction from raw markdown context when available."""
        claims: List[Dict[str, Any]] = []
        for md_file in context_dir.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                lowered = content.lower()
                source = md_file.stem

                if "deadhang" in source.lower() and "ssl" in lowered:
                    claims.append(
                        self.make_claim(
                            "project",
                            "Deadhang website SSL/security implementation",
                            "pillar-1",
                            source,
                            "active",
                            evidence="Raw context fallback: Deadhang active website item",
                        )
                    )

                if "crew_blueprint" in source.lower() and "disabled the lms" in lowered:
                    claims.append(
                        self.make_claim(
                            "blocker",
                            "Crew Blueprint LMS remains paused",
                            "pillar-2",
                            source,
                            "blocked",
                            evidence="Raw context fallback: LMS pause decision",
                        )
                    )

                if "production_atlas" in source.lower() and "human verification" in lowered:
                    claims.append(
                        self.make_claim(
                            "blocker",
                            "Production Atlas public research has verification gaps",
                            "pillar-3",
                            source,
                            "blocked",
                            evidence="Raw context fallback: public research limitations",
                        )
                    )
            except Exception as exc:
                print(f"  ⚠️  Skipped {md_file.name}: {exc}")
        return claims

    def dedupe_claims(self, claims: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Deduplicate exact title/status/pillar/source repeats while keeping separate digest evidence."""
        seen = set()
        unique: List[Dict[str, Any]] = []
        for claim in claims:
            key = (
                claim.get("type"),
                claim.get("description", "").strip().lower(),
                claim.get("pillar"),
                claim.get("status"),
                claim.get("source"),
            )
            if key in seen:
                continue
            seen.add(key)
            unique.append(claim)
        return unique

    def map_claims_to_projects(self) -> Dict[str, List[Dict[str, Any]]]:
        projects_by_pillar = {p: [] for p in PILLARS.keys()}
        for claim in self.claims:
            pillar = claim.get("pillar", "pillar-7")
            if pillar in projects_by_pillar:
                projects_by_pillar[pillar].append(claim)
        return projects_by_pillar

    def calculate_frontier(self, projects_by_pillar: Dict[str, List[Dict[str, Any]]]) -> Optional[Dict[str, Any]]:
        """Calculate the 'You Are Now Here' frontier."""
        print("🎯 Calculating next priority...")
        candidates: List[Dict[str, Any]] = []
        deep_context_pillars = {
            pillar
            for source in self.deep_context_sources
            for pillar in source.get("pillars", [])
        }

        for pillar_id, pillar in PILLARS.items():
            claims = projects_by_pillar.get(pillar_id, [])
            active_claims = [c for c in claims if c.get("status") == "active"]
            blockers = [c for c in claims if c.get("status") == "blocked"]

            # Future pillars stay out unless their digests show active work now.
            if pillar["status"] != "active" and not active_claims:
                continue

            if not active_claims and not blockers:
                continue

            score = PRIORITY_SCORES.get(pillar["priority"], 0)
            score += min(len(active_claims), 8)
            score += min(len(blockers), 5) * 0.5

            candidates.append(
                {
                    "pillar_id": pillar_id,
                    "pillar_title": pillar["title"],
                    "priority": pillar["priority"],
                    "score": score,
                    "active_work": len(active_claims),
                    "blockers": len(blockers),
                    "deep_context_referenced": pillar_id in deep_context_pillars,
                }
            )

        candidates.sort(key=lambda item: (-item["score"], -item["active_work"], -item["blockers"], item["pillar_id"]))

        if not candidates:
            return None

        frontier = candidates[0]
        frontier["reasoning"] = (
            f"{frontier['priority'].title()} priority + "
            f"{frontier['active_work']} active items + "
            f"{frontier['blockers']} blockers"
        )
        if frontier.get("deep_context_referenced"):
            frontier["reasoning"] += " + deep-context alignment check required"
        return frontier

    def add_project_proposal(self, claim: Dict[str, Any]) -> None:
        self.proposals["projects"].append(
            {
                "id": f"project-{len(self.proposals['projects'])}",
                "title": claim.get("description"),
                "status": "active",
                "priority": claim.get("priority", "medium"),
                "pillar_id": claim.get("pillar"),
                "evidence": claim.get("evidence"),
            }
        )

    def add_completed_proposal(self, claim: Dict[str, Any]) -> None:
        self.proposals["completed"].append(
            {
                "id": f"task-{len(self.proposals['completed'])}",
                "title": claim.get("description"),
                "status": "completed",
                "pillar_id": claim.get("pillar"),
                "evidence": claim.get("evidence"),
            }
        )

    def add_blocker_proposal(self, claim: Dict[str, Any]) -> None:
        self.proposals["blockers"].append(
            {
                "id": f"blocker-{len(self.proposals['blockers'])}",
                "title": claim.get("description"),
                "status": "blocked",
                "pillar_id": claim.get("pillar"),
                "evidence": claim.get("evidence"),
                "action": "REQUIRES DECISION: Resolve or defer?",
            }
        )

    def add_moved_later_proposal(self, claim: Dict[str, Any]) -> None:
        self.proposals["moved_later"].append(
            {
                "id": f"deferred-{len(self.proposals['moved_later'])}",
                "title": claim.get("description"),
                "status": "moved_later",
                "reason": "Deferred to protect the primary path",
                "pillar_id": claim.get("pillar"),
                "evidence": claim.get("evidence"),
            }
        )

    def generate_proposals(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate roadmap update proposals based on normalized claim status."""
        print("✍️  Generating roadmap proposals...")
        projects_by_pillar = self.map_claims_to_projects()
        self.frontier = self.calculate_frontier(projects_by_pillar)

        for claim in self.claims:
            status = claim.get("status")
            claim_type = claim.get("type")

            if status == "completed":
                self.add_completed_proposal(claim)
            elif status == "blocked" or claim_type == "blocker":
                self.add_blocker_proposal(claim)
            elif status == "moved_later":
                self.add_moved_later_proposal(claim)
            elif status == "active" or claim_type in PROJECT_TYPES:
                self.add_project_proposal(claim)

        return self.proposals

    def report(self) -> str:
        """Generate Aaron-style report: direct, factual, actionable."""
        lines = [
            "═" * 70,
            "🎯 ROADMAP WATCHER REPORT",
            "═" * 70,
            f"Generated: {datetime.now().isoformat()}",
            "",
        ]

        if self.frontier:
            lines.extend(
                [
                    "📍 YOU ARE NOW HERE:",
                    f"  Pillar: {self.frontier['pillar_title']}",
                    f"  Priority: {self.frontier['priority'].upper()}",
                    f"  Active work: {self.frontier['active_work']} items",
                    f"  Blockers: {self.frontier['blockers']}",
                    f"  Deep context referenced: {self.frontier.get('deep_context_referenced', False)}",
                    f"  Reasoning: {self.frontier['reasoning']}",
                    "",
                ]
            )

        lines.extend(
            [
                "📚 DEEP-CONTEXT DECISION SOURCES:",
                f"  Loaded: {len(self.deep_context_sources)} files",
            ]
        )
        for source in self.deep_context_sources[:10]:
            lines.append(f"  - {source['path']} → {', '.join(source.get('pillars', []))}")
        if len(self.deep_context_sources) > 10:
            lines.append(f"  ... {len(self.deep_context_sources) - 10} more deep-context files")
        lines.append("")

        lines.extend(
            [
                "📊 ROADMAP PROPOSALS:",
                f"  Active projects: {len(self.proposals['projects'])}",
                f"  Completed: {len(self.proposals['completed'])}",
                f"  Deferred (moved later): {len(self.proposals['moved_later'])}",
                f"  Blockers: {len(self.proposals['blockers'])}",
                "",
            ]
        )

        if self.proposals["blockers"]:
            lines.extend(["⚠️  BLOCKERS (REQUIRE DECISION):", ""])
            for blocker in self.proposals["blockers"][:30]:
                lines.append(f"  - [{blocker['pillar_id']}] {blocker['title']}")
                lines.append(f"    Evidence: {blocker['evidence']}")
                lines.append(f"    Action: {blocker['action']}")
                lines.append("")
            if len(self.proposals["blockers"]) > 30:
                lines.append(f"  ... {len(self.proposals['blockers']) - 30} more blockers in watcher-proposals.json")
                lines.append("")

        lines.extend(
            [
                "✅ NEXT STEPS:",
                "  1. Review watcher-proposals.json.",
                "  2. Check deep-context decision sources before changing direction or priority.",
                "  3. Resolve or move later the highest-impact blockers.",
                "  4. Keep the primary path linear; do not let side projects erase active work.",
                "═" * 70,
            ]
        )
        return "\n".join(lines)

    def save_proposals(self) -> bool:
        """Save proposals as JSON for review."""
        output_file = DATA_DIR / "roadmap" / "watcher-proposals.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "generated_at": datetime.now().isoformat(),
                        "frontier": self.frontier,
                        "decision_context": {
                            "deep_context_policy": "Consult these files before changing frontier, sequencing, pillar priority, project boundaries, or public-safe summaries. Do not publish raw deep-context material.",
                            "sources": self.deep_context_sources,
                        },
                        "proposals": self.proposals,
                    },
                    f,
                    indent=2,
                )
            print(f"✓ Proposals saved to {output_file}")
            return True
        except Exception as exc:
            print(f"❌ Failed to save proposals: {exc}")
            return False

    def run(self) -> bool:
        """Run the complete watcher workflow."""
        print("\n🤖 ROADMAP WATCHER STARTING")
        print("   Mode: Evidence-based, public-safe extraction + deep-context decision awareness")
        print()

        self.load_memory_index()

        if not self.extract_claims_from_context():
            return False

        self.generate_proposals()
        self.save_proposals()
        print(self.report())
        print("\n💡 RECOMMENDATION:")
        print("   These proposals are auditable, evidence-linked, and public-safe.")
        print("   Deep-context files are decision context, not raw public output.")
        print("   Review the blockers; they are the gating items.")
        print("   Move side quests later instead of losing them.")
        print()
        return True


if __name__ == "__main__":
    watcher = RoadmapWatcher()
    success = watcher.run()
    sys.exit(0 if success else 1)
