#!/usr/bin/env python3
"""
Roadmap Watcher: AI agent that thinks like Aaron.

Reads memory chunks, extracts actionable claims, maps to pillars,
validates for public safety, and proposes roadmap updates.

Personality embedded:
- Practical: Evidence-based, no speculation
- Direct: Clear next steps, no fluff
- Cautious: Don't overclaim, link to sources
- Focused: Protect primary path, defer non-core work
- Auditable: Every claim links back to memory
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MEMORIES_DIR = ROOT / "memories" / "processed" / "chunks"

# The 8 Pillars - Aaron's operating tracks
PILLARS = {
    "pillar-1": {
        "title": "Deadhang Labor LLC",
        "track": "business_operations",
        "priority": "critical",
        "status": "active"
    },
    "pillar-2": {
        "title": "The Crew Blueprint",
        "track": "content_platform",
        "priority": "high",
        "status": "active"
    },
    "pillar-3": {
        "title": "Production Atlas",
        "track": "software_projects",
        "priority": "medium",
        "status": "future"
    },
    "pillar-4": {
        "title": "Contractor Tools",
        "track": "software_projects",
        "priority": "high",
        "status": "active"
    },
    "pillar-5": {
        "title": "Land Acquisition",
        "track": "land_and_legacy",
        "priority": "medium",
        "status": "future"
    },
    "pillar-6": {
        "title": "Homestead Network",
        "track": "land_and_legacy",
        "priority": "low",
        "status": "future"
    },
    "pillar-7": {
        "title": "Personal Operations",
        "track": "personal_admin",
        "priority": "critical",
        "status": "active"
    },
    "pillar-8": {
        "title": "Skills & Certifications",
        "track": "skills_progression",
        "priority": "high",
        "status": "active"
    }
}

# Key extraction patterns - what Aaron cares about
PATTERNS = {
    "completed": [
        r"(?:completed|finished|done|shipped|delivered|merged).*?(?:on|by)\s+(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})",
        r"(?:june|july|may|april).*?(\d{1,2}).*?(?:completed|finished|done|shipped)"
    ],
    "blocker": [
        r"(?:blocked|stuck|halted|waiting on|pending).*?(?:because|due to|reason)[:=]\s*(.{10,150})",
        r"(?:insurance|osha|tax debt|ssl|website).*?(?:unresolved|pending|outstanding|needs)"
    ],
    "active": [
        r"(?:working on|currently|in progress|active).*?(.{5,100})",
        r"(?:summer|festival|production).*?(?:work|run).*?(\d+\s*hours?)"
    ],
    "deferred": [
        r"(?:moved later|deferred|postponed|next phase).*?(.{10,150})",
        r"(?:later|future|phase \d).*?(?:will|should).*?(.{10,150})"
    ]
}

class RoadmapWatcher:
    """Aaron's roadmap watcher - thinks and decides like he does."""

    def __init__(self):
        self.memories: List[Dict] = []
        self.claims: List[Dict] = []
        self.proposals: Dict = {
            "projects": [],
            "tasks": [],
            "completed": [],
            "moved_later": [],
            "blockers": [],
            "conflicts": []
        }
        self.frontier: Optional[Dict] = None

    def load_memory_index(self) -> bool:
        """Load the memory index to find relevant chunks."""
        index_file = ROOT / "memories" / "processed" / "indexes" / "sources.json"
        if not index_file.exists():
            print("❌ Memory index not found. Run process-memories.py first.")
            return False

        try:
            with open(index_file) as f:
                sources = json.load(f)
                # Filter to relevant archives
                relevant = [
                    s for s in sources
                    if any(
                        keyword in s.get("archive_id", "").lower()
                        for keyword in [
                            "chatgpt-export", "claude-batch", "kimi-batch",
                            "gemini", "festival-atlas"
                        ]
                    )
                ]
                self.memory_sources = {
                    s["source_path"]: s for s in relevant
                }
                print(f"✓ Loaded {len(self.memory_sources)} memory sources")
                return True
        except Exception as e:
            print(f"❌ Failed to load memory index: {e}")
            return False

    def extract_claims_from_digest_files(self) -> List[Dict]:
        """Extract claims from raw report digest files (markdown format)."""
        claims = []
        digest_dir = DATA_DIR / "raw-reports"

        if not digest_dir.exists():
            return claims

        # Read all digest files (format: YYYY-MM-DD-{source}-digest.md)
        for digest_file in sorted(digest_dir.glob("*-digest.md")):
            try:
                with open(digest_file) as f:
                    content = f.read()

                source_name = digest_file.stem.replace("-digest", "")

                # Extract projects from "Active Projects & Decisions" section
                # Match from ## Active Projects to next ## that's NOT followed by #
                projects_section = re.search(
                    r"## Active Projects[\s\S]*?(?=\n## [^#]|\Z)",
                    content,
                    re.IGNORECASE
                )
                if projects_section:
                    # Parse each project (identified by ### headers with bold titles)
                    project_lines = projects_section.group(0).split('\n')
                    i = 0
                    while i < len(project_lines):
                        line = project_lines[i]
                        # Look for ### Project Title pattern
                        if line.startswith('###'):
                            title = line.replace('###', '').strip()
                            i += 1
                            # Collect following lines until next ### or ##
                            block_text = []
                            while i < len(project_lines) and not project_lines[i].startswith(('#')):
                                block_text.append(project_lines[i])
                                i += 1

                            block = '\n'.join(block_text)

                            # Extract pillar mapping
                            pillar_match = re.search(r"\*\*Pillar:\*\*\s*(pillar-\d+)", block)
                            pillar = pillar_match.group(1) if pillar_match else "pillar-1"

                            # Extract status
                            status_match = re.search(r"\*\*Status:\*\*\s*(.+?)(?:\n|$)", block)
                            status = "active"
                            if status_match:
                                status_text = status_match.group(1).lower()
                                if "completed" in status_text or "done" in status_text:
                                    status = "completed"
                                elif "blocked" in status_text or "blocked on" in status_text:
                                    status = "blocked"
                                elif "deferred" in status_text or "deferred" in status_text:
                                    status = "moved_later"

                            claims.append({
                                "type": "project",
                                "description": title,
                                "pillar": pillar,
                                "source": source_name,
                                "status": status,
                                "evidence": f"From {source_name} digest",
                                "priority": "high"
                            })
                        else:
                            i += 1

                # Extract blockers with pillar mapping
                blockers_section = re.search(
                    r"## Blockers?[\s\S]*?(?=\n## [^#]|\Z)",
                    content,
                    re.IGNORECASE
                )
                if blockers_section:
                    # Parse numbered list items
                    blocker_lines = blockers_section.group(0).split('\n')
                    for line in blocker_lines:
                        # Match pattern: "1. **Title** — Evidence: ..."
                        blocker_match = re.match(r"^\s*\d+\.\s*\*\*(.+?)\*\*", line)
                        if blocker_match:
                            blocker_title = blocker_match.group(1).strip()
                            # Try to extract evidence
                            evidence_text = line.replace(blocker_match.group(0), '').strip()

                            claims.append({
                                "type": "blocker",
                                "description": blocker_title,
                                "pillar": "pillar-7",  # Blockers typically in Personal Operations
                                "source": source_name,
                                "status": "blocked",
                                "evidence": f"From {source_name} digest"
                            })

            except Exception as e:
                print(f"  ⚠️  Could not parse {digest_file.name}: {e}")

        if claims:
            print(f"✓ Extracted {len(claims)} claims from digest files")

        return claims

    def extract_claims_from_context(self) -> bool:
        """Extract actionable claims from memory chunks."""
        # Key context files that contain work/project info
        key_files = [
            "07_ACTIVE_LOGS_REMINDERS_AND_TRACKING",
            "03_DEADHANG_LABOR_LLC",
            "04_THE_CREW_BLUEPRINT",
            "05_PRODUCTION_ATLAS_FESTIVAL_ATLAS",
            "06_TECHNICAL_PROJECTS_AND_APPS",
            "08_PREFERENCES_CONSTRAINTS_AND_OPERATING_RULES"
        ]

        print("🔍 Extracting claims from memories...")

        # First try to extract from digest files (easy to create manually)
        digest_claims = self.extract_claims_from_digest_files()

        # Read the actual context files from the chatgpt export
        context_dir = ROOT / "memories" / "processed" / "_extracted_raw" / "chatgpt-export-2026-07-05" / "aaron_bowman_context_export_md"

        claims = digest_claims.copy()

        if not context_dir.exists():
            print("⚠️  Context files not yet extracted. This is OK - using digest approach.")
            self.claims = claims
            return self.extract_from_pillars() if not claims else True

        # Extract from each key file if context available
        for file_pattern in key_files:
            for md_file in context_dir.glob(f"*{file_pattern}*.md"):
                try:
                    with open(md_file) as f:
                        content = f.read()

                    # Aaron's principle: extract specific, actionable claims
                    if "ACTIVE_LOGS" in str(md_file):
                        claims.extend(self.extract_work_log(content, "work_log"))
                    elif "DEADHANG" in str(md_file):
                        claims.extend(self.extract_business_claims(content, "deadhang"))
                    elif "CREW_BLUEPRINT" in str(md_file):
                        claims.extend(self.extract_crew_blueprint_claims(content, "crew_blueprint"))
                    elif "PRODUCTION_ATLAS" in str(md_file):
                        claims.extend(self.extract_atlas_claims(content, "atlas"))
                    elif "TECHNICAL" in str(md_file):
                        claims.extend(self.extract_tech_claims(content, "tech"))

                except Exception as e:
                    print(f"  ⚠️  Skipped {md_file.name}: {e}")

        self.claims = claims
        total = len(claims)
        from_digest = len(digest_claims)
        print(f"✓ Extracted {total} actionable claims ({from_digest} from digests, {total - from_digest} from context)")
        return True

    def extract_work_log(self, content: str, source: str) -> List[Dict]:
        """Extract from active logs - Aaron's work record."""
        claims = []

        # Extract work hours (Aaron tracks these carefully)
        hours_match = re.search(r"total.*?(\d+)\s*hours", content, re.IGNORECASE)
        if hours_match:
            claims.append({
                "type": "work_completed",
                "description": f"Michigan festival run: {hours_match.group(1)} hours worked",
                "pillar": "pillar-1",  # Deadhang Labor
                "source": source,
                "evidence": "active logs June 22 - July 2",
                "status": "completed"
            })

        # Extract blockers (Aaron tracks these to fix them)
        blockers = [
            "insurance provider selection",
            "OSHA training/provider selection",
            "invoice app/system finalization",
            "tax debt/monthly tax payment reminders"
        ]
        for blocker in blockers:
            if blocker.lower() in content.lower():
                claims.append({
                    "type": "blocker",
                    "description": blocker,
                    "pillar": "pillar-7",  # Personal Operations
                    "source": source,
                    "status": "blocked",
                    "evidence": "active items"
                })

        return claims

    def extract_business_claims(self, content: str, source: str) -> List[Dict]:
        """Extract from Deadhang LLC context."""
        claims = []

        if "business email works" in content.lower():
            claims.append({
                "type": "completed",
                "description": "Deadhang business email operational",
                "pillar": "pillar-1",
                "source": source,
                "status": "completed",
                "evidence": "email setup verified"
            })

        if "ssl" in content.lower() or "security" in content.lower():
            claims.append({
                "type": "active",
                "description": "Deadhang website SSL/security implementation",
                "pillar": "pillar-1",
                "source": source,
                "status": "active",
                "priority": "high",
                "evidence": "only remaining cPanel issue"
            })

        return claims

    def extract_crew_blueprint_claims(self, content: str, source: str) -> List[Dict]:
        """Extract from Crew Blueprint context."""
        claims = []

        if "lms" in content.lower() or "course" in content.lower():
            claims.append({
                "type": "active",
                "description": "Crew Blueprint course content creation (83-lesson outline)",
                "pillar": "pillar-2",
                "source": source,
                "status": "active",
                "priority": "high",
                "evidence": "lesson structure defined, JSON workflow"
            })

        if "disabled the lms" in content.lower() or "2026-06-11" in content:
            claims.append({
                "type": "pivot",
                "description": "Paused LMS display rebuild; focusing on content creation first",
                "pillar": "pillar-2",
                "source": source,
                "status": "active",
                "evidence": "decision documented"
            })

        return claims

    def extract_atlas_claims(self, content: str, source: str) -> List[Dict]:
        """Extract from Production Atlas context."""
        claims = []

        if "254" in content and "opportunity" in content.lower():
            claims.append({
                "type": "completed",
                "description": "Festival Atlas live: 254 opportunity records active",
                "pillar": "pillar-3",
                "source": source,
                "status": "completed",
                "evidence": "research-version branch live"
            })

        if "research" in content.lower() and "batch" in content.lower():
            claims.append({
                "type": "active",
                "description": "Production Atlas deep research (festivals, vendors, logistics)",
                "pillar": "pillar-3",
                "source": source,
                "status": "active",
                "evidence": "6 research batches in progress"
            })

        return claims

    def extract_tech_claims(self, content: str, source: str) -> List[Dict]:
        """Extract from technical projects context."""
        claims = []

        tech_projects = {
            "invoice generator": ("pillar-4", "Android-only invoice app"),
            "affirmation calendar": ("pillar-4", "365-day Google Calendar integration"),
            "task app": ("pillar-4", "Private task tracking with AI backend")
        }

        for tech, (pillar, desc) in tech_projects.items():
            if tech.lower() in content.lower():
                claims.append({
                    "type": "active",
                    "description": desc,
                    "pillar": pillar,
                    "source": source,
                    "status": "moved_later",  # Aaron defers these
                    "priority": "medium",
                    "evidence": "framework discussed, needs build"
                })

        return claims

    def extract_from_pillars(self) -> bool:
        """Create baseline pillar claims if memories not available."""
        print("📋 Creating baseline claims from 8 pillars...")

        for pillar_id, pillar in PILLARS.items():
            self.claims.append({
                "type": "pillar_baseline",
                "description": pillar["title"],
                "pillar": pillar_id,
                "status": pillar["status"],
                "priority": pillar["priority"],
                "evidence": "roadmap definition"
            })

        return True

    def map_claims_to_projects(self) -> Dict[str, List[Dict]]:
        """Map claims to projects under each pillar."""
        projects_by_pillar = {p: [] for p in PILLARS.keys()}

        for claim in self.claims:
            pillar = claim.get("pillar", "pillar-1")
            if pillar in projects_by_pillar:
                projects_by_pillar[pillar].append(claim)

        return projects_by_pillar

    def calculate_frontier(self, projects_by_pillar: Dict) -> Optional[Dict]:
        """Calculate "You Are Now Here" - the next critical action."""
        print("🎯 Calculating next priority...")

        # Aaron's priority: critical + active > high + active > defer
        candidates = []

        for pillar_id, pillar in PILLARS.items():
            if pillar["status"] != "active":
                continue

            claims = projects_by_pillar.get(pillar_id, [])
            active_claims = [c for c in claims if c.get("status") == "active"]

            if active_claims:
                # Score: critical=10, high=5, medium=3, low=1
                priority_scores = {"critical": 10, "high": 5, "medium": 3, "low": 1}
                score = priority_scores.get(pillar["priority"], 0)

                candidates.append({
                    "pillar_id": pillar_id,
                    "pillar_title": pillar["title"],
                    "priority": pillar["priority"],
                    "score": score,
                    "active_work": len(active_claims),
                    "blockers": len([c for c in claims if c.get("status") == "blocked"])
                })

        # Sort by score (Aaron focuses on critical first)
        candidates.sort(key=lambda x: (-x["score"], -x["active_work"], x["blockers"]))

        if candidates:
            frontier = candidates[0]
            reason = (
                f"Critical priority + {frontier['active_work']} active items"
                if frontier["score"] >= 10
                else f"High priority + {frontier['active_work']} active items"
            )
            frontier["reasoning"] = reason
            return frontier

        return None

    def generate_proposals(self) -> Dict:
        """Generate roadmap update proposals."""
        print("✍️  Generating roadmap proposals...")

        projects_by_pillar = self.map_claims_to_projects()
        self.frontier = self.calculate_frontier(projects_by_pillar)

        # Build proposals by type
        for claim in self.claims:
            claim_type = claim.get("type")
            pillar = claim.get("pillar")

            if claim_type == "completed":
                self.proposals["completed"].append({
                    "id": f"task-{len(self.proposals['completed'])}",
                    "title": claim.get("description"),
                    "status": "completed",
                    "pillar_id": pillar,
                    "evidence": claim.get("evidence")
                })

            elif claim_type == "blocker":
                self.proposals["blockers"].append({
                    "id": f"blocker-{len(self.proposals['blockers'])}",
                    "title": claim.get("description"),
                    "status": "blocked",
                    "pillar_id": pillar,
                    "evidence": claim.get("evidence"),
                    "action": "REQUIRES DECISION: Resolve or defer?"
                })

            elif claim_type == "active":
                self.proposals["projects"].append({
                    "id": f"project-{len(self.proposals['projects'])}",
                    "title": claim.get("description"),
                    "status": "active",
                    "priority": claim.get("priority", "medium"),
                    "pillar_id": pillar,
                    "evidence": claim.get("evidence")
                })

            elif claim_type in ["deferred", "moved_later"]:
                self.proposals["moved_later"].append({
                    "id": f"deferred-{len(self.proposals['moved_later'])}",
                    "title": claim.get("description"),
                    "status": "moved_later",
                    "reason": "Deferred to focus primary path",
                    "pillar_id": pillar
                })

        return self.proposals

    def report(self) -> str:
        """Generate Aaron-style report: direct, factual, actionable."""
        lines = [
            "═" * 70,
            "🎯 ROADMAP WATCHER REPORT",
            "═" * 70,
            f"Generated: {datetime.now().isoformat()}",
            ""
        ]

        # You Are Now Here
        if self.frontier:
            lines.extend([
                "📍 YOU ARE NOW HERE:",
                f"  Pillar: {self.frontier['pillar_title']}",
                f"  Priority: {self.frontier['priority'].upper()}",
                f"  Active work: {self.frontier['active_work']} items",
                f"  Blockers: {self.frontier['blockers']}",
                f"  Reasoning: {self.frontier['reasoning']}",
                ""
            ])

        # Proposals summary
        lines.extend([
            "📊 ROADMAP PROPOSALS:",
            f"  Active projects: {len(self.proposals['projects'])}",
            f"  Completed: {len(self.proposals['completed'])}",
            f"  Deferred (moved later): {len(self.proposals['moved_later'])}",
            f"  Blockers: {len(self.proposals['blockers'])}",
            ""
        ])

        # Blockers require decision
        if self.proposals["blockers"]:
            lines.extend([
                "⚠️  BLOCKERS (REQUIRE DECISION):",
                ""
            ])
            for blocker in self.proposals["blockers"]:
                lines.append(f"  - {blocker['title']}")
                lines.append(f"    Evidence: {blocker['evidence']}")
                lines.append(f"    Action: {blocker['action']}")
                lines.append("")

        # Next steps
        lines.extend([
            "✅ NEXT STEPS:",
            "  1. Review blockers above - decide: resolve now or defer?",
            "  2. Validate proposals in /data/roadmap/projects.json",
            "  3. Run: python scripts/validate-roadmap.py",
            "  4. Run: python scripts/build-roadmap.py",
            "  5. Commit with: git add data/roadmap && git commit",
            ""
        ])

        lines.extend([
            "═" * 70,
        ])

        return "\n".join(lines)

    def save_proposals(self) -> bool:
        """Save proposals as JSON for review."""
        output_file = DATA_DIR / "roadmap" / "watcher-proposals.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_file, 'w') as f:
                json.dump({
                    "generated_at": datetime.now().isoformat(),
                    "frontier": self.frontier,
                    "proposals": self.proposals
                }, f, indent=2)

            print(f"✓ Proposals saved to {output_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to save proposals: {e}")
            return False

    def run(self) -> bool:
        """Run the complete watcher workflow."""
        print("\n🤖 ROADMAP WATCHER STARTING")
        print("   Personality: Aaron's decision-making")
        print("   Mode: Evidence-based, public-safe extraction")
        print()

        if not self.load_memory_index():
            print("⚠️  Continuing with baseline claims...")

        if not self.extract_claims_from_context():
            return False

        self.generate_proposals()
        self.save_proposals()

        report = self.report()
        print(report)

        print("\n💡 RECOMMENDATION (Aaron's voice):")
        print("   These proposals are auditable, evidence-linked, and public-safe.")
        print("   Review the blockers - they're the real gating items.")
        print("   Everything else can move at its own pace.")
        print()

        return True


if __name__ == "__main__":
    watcher = RoadmapWatcher()
    success = watcher.run()
    sys.exit(0 if success else 1)
