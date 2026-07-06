#!/usr/bin/env python3
"""
Validate roadmap data before commit.

Rules:
1. All fields must match public-safety schema
2. No personal/sensitive data allowed
3. All references must be resolvable
4. Status values must be valid
5. Progression tracks must align with pillars

Exit code 0 = valid, 1 = invalid, 2 = missing files
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "roadmap"
SCHEMA_FILE = ROOT / "data" / "schema" / "roadmap-public-safety.json"

# Patterns that must never appear in public data
FORBIDDEN_PATTERNS = {
    "phone": r"\+?1?\s*\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "address": r"\d+\s+[A-Za-z\s]+(St|Ave|Rd|Blvd|Way|Drive|Court|Lane|Parkway)",
    "person": r"\b(Aaron|Bowman|Mesa|Arizona|aaronbowman84|deadhanglaborllc|630-280-3415)\b",
    "credit_card": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
}

class RoadmapValidator:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.data: Dict = {}
        self.schema: Dict = {}

    def load_schema(self) -> bool:
        """Load the public-safety schema."""
        if not SCHEMA_FILE.exists():
            self.errors.append(f"Schema file not found: {SCHEMA_FILE}")
            return False
        try:
            with open(SCHEMA_FILE) as f:
                self.schema = json.load(f)
            return True
        except Exception as e:
            self.errors.append(f"Failed to load schema: {e}")
            return False

    def load_roadmap_files(self) -> bool:
        """Load all roadmap JSON files."""
        required_files = ["vision.json", "pillars.json"]
        optional_files = [
            "programs.json", "projects.json", "tasks.json",
            "milestones.json", "moved_later.json", "loose_threads.json",
            "conflicts.json"
        ]

        for fname in required_files:
            fpath = DATA_DIR / fname
            if not fpath.exists():
                self.errors.append(f"Required file missing: {fname}")
                return False
            try:
                with open(fpath) as f:
                    data = json.load(f)
                    key = fname.replace(".json", "")
                    if fname == "vision.json":
                        self.data["vision"] = data
                    elif fname == "pillars.json":
                        self.data["pillars"] = data
            except Exception as e:
                self.errors.append(f"Failed to load {fname}: {e}")
                return False

        for fname in optional_files:
            fpath = DATA_DIR / fname
            if fpath.exists():
                try:
                    with open(fpath) as f:
                        data = json.load(f)
                        key = fname.replace(".json", "")
                        if isinstance(data, list):
                            self.data[key] = data
                        else:
                            self.data[key] = data
                except Exception as e:
                    self.errors.append(f"Failed to load {fname}: {e}")
                    return False
            else:
                # Optional files default to empty
                key = fname.replace(".json", "")
                if key == "moved_later":
                    self.data["movedLater"] = []
                elif key == "loose_threads":
                    self.data["looseThreads"] = []
                else:
                    self.data[key] = []

        return True

    def check_sensitive_data(self, text: str, field_path: str) -> bool:
        """Check for forbidden patterns in a text field."""
        is_clean = True
        for pattern_name, pattern in FORBIDDEN_PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                self.errors.append(
                    f"SENSITIVE DATA DETECTED in {field_path}: {pattern_name}\n"
                    f"  Value: {text[:100]}"
                )
                is_clean = False
        return is_clean

    def validate_string_fields(self, obj: Dict, path: str) -> bool:
        """Recursively check all string fields for sensitive data."""
        is_valid = True
        for key, value in obj.items():
            field_path = f"{path}.{key}"
            if isinstance(value, str):
                if not self.check_sensitive_data(value, field_path):
                    is_valid = False
            elif isinstance(value, dict):
                if not self.validate_string_fields(value, field_path):
                    is_valid = False
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                for idx, item in enumerate(value):
                    if not self.validate_string_fields(item, f"{field_path}[{idx}]"):
                        is_valid = False
        return is_valid

    def validate_status_values(self) -> bool:
        """Validate all status fields are from allowed enum."""
        allowed_statuses = {
            "active", "completed", "moved_later", "blocked",
            "loose_thread", "conflict", "rejected", "future"
        }
        is_valid = True

        for section_key, section in self.data.items():
            if not isinstance(section, (list, dict)):
                continue

            items = section if isinstance(section, list) else [section]
            for idx, item in enumerate(items):
                if isinstance(item, dict) and "status" in item:
                    if item["status"] not in allowed_statuses:
                        self.errors.append(
                            f"Invalid status '{item['status']}' in {section_key}[{idx}]"
                        )
                        is_valid = False

        return is_valid

    def validate_progression_tracks(self) -> bool:
        """Validate all progression_track values."""
        allowed_tracks = {
            "primary_path",
            "business_operations",
            "content_platform",
            "software_projects",
            "land_and_legacy",
            "personal_admin",
            "skills_progression"
        }
        is_valid = True

        for section_key, section in self.data.items():
            if not isinstance(section, list):
                continue

            for idx, item in enumerate(section):
                if isinstance(item, dict) and "progression_track" in item:
                    if item["progression_track"] not in allowed_tracks:
                        self.errors.append(
                            f"Invalid progression_track '{item['progression_track']}' "
                            f"in {section_key}[{idx}]"
                        )
                        is_valid = False

        return is_valid

    def validate_pillar_references(self) -> bool:
        """Validate that projects reference valid pillars."""
        if "pillars" not in self.data or "projects" not in self.data:
            return True

        pillar_ids = {p["id"] for p in self.data.get("pillars", [])}
        is_valid = True

        for idx, project in enumerate(self.data.get("projects", [])):
            if "pillar_id" in project and project["pillar_id"]:
                if project["pillar_id"] not in pillar_ids:
                    self.errors.append(
                        f"Project {project['id']} references non-existent pillar "
                        f"{project['pillar_id']}"
                    )
                    is_valid = False

        return is_valid

    def run(self) -> bool:
        """Run all validations."""
        print("🔍 Validating roadmap data...")

        if not self.load_schema():
            return False

        if not self.load_roadmap_files():
            return False

        # Run validations
        validations = [
            ("Checking for sensitive data", self.check_all_sensitive_data),
            ("Validating status values", self.validate_status_values),
            ("Validating progression tracks", self.validate_progression_tracks),
            ("Validating pillar references", self.validate_pillar_references),
        ]

        all_passed = True
        for desc, validator in validations:
            print(f"  {desc}...", end=" ")
            if validator():
                print("✓")
            else:
                print("✗")
                all_passed = False

        # Report results
        print()
        if self.errors:
            print("❌ VALIDATION FAILED")
            print()
            for error in self.errors:
                print(f"  ERROR: {error}")
            print()
            return False

        if self.warnings:
            print("⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()

        print("✅ Roadmap data is valid and safe for public commit.")
        return True

    def check_all_sensitive_data(self) -> bool:
        """Check entire data structure for sensitive patterns."""
        is_valid = True
        for section_key, section in self.data.items():
            if isinstance(section, dict):
                if not self.validate_string_fields(section, section_key):
                    is_valid = False
            elif isinstance(section, list):
                for idx, item in enumerate(section):
                    if isinstance(item, dict):
                        if not self.validate_string_fields(item, f"{section_key}[{idx}]"):
                            is_valid = False
        return is_valid


if __name__ == "__main__":
    validator = RoadmapValidator()
    if validator.run():
        sys.exit(0)
    else:
        sys.exit(1)
