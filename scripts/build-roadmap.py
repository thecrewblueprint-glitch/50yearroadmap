#!/usr/bin/env python3
"""
Legacy pillar-model roadmap compiler.

WARNING / CONTEXT
-----------------
This compiles the *pillar* data model (data/roadmap/*.json) into a single
JSON document. It is NOT the data model the live dashboard reads.

The live dashboard (index.html + app.js) reads the root ``roadmap.json`` in
the *branch* model: ``ultimate_goal``, ``phase``, ``branches``,
``this_week_focus``, ``ecosystem_flow``. Those two shapes are incompatible.

To avoid silently destroying the live dashboard, this script writes to a
build artifact (``data/roadmap/compiled.json``) and NEVER overwrites the
root ``roadmap.json``. It also reports which expected input files are
missing instead of quietly emitting empty arrays.
"""

import json
import os

# Inputs for the (legacy) pillar model. Only vision.json and pillars.json
# currently exist; the rest are part of a pipeline that was never built out.
INPUTS = {
    "vision": "data/roadmap/vision.json",
    "pillars": "data/roadmap/pillars.json",
    "programs": "data/roadmap/programs.json",
    "projects": "data/roadmap/projects.json",
    "milestones": "data/roadmap/milestones.json",
    "tasks": "data/roadmap/tasks.json",
    "movedLater": "data/roadmap/moved_later.json",
    "looseThreads": "data/roadmap/loose_threads.json",
    "conflicts": "data/roadmap/conflicts.json",
}

OUTPUT_PATH = "data/roadmap/compiled.json"


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def build():
    roadmap = {}
    missing = []
    for key, path in INPUTS.items():
        data = load_json(path)
        if data is None:
            missing.append(path)
            roadmap[key] = []
        else:
            roadmap[key] = data

    with open(OUTPUT_PATH, "w") as f:
        json.dump(roadmap, f, indent=2)

    print(f"✅ Legacy pillar model compiled to {OUTPUT_PATH}")
    if missing:
        print("⚠️  Missing expected inputs (emitted as empty arrays):")
        for path in missing:
            print(f"     - {path}")
    print("ℹ️  This did NOT touch the live dashboard file (root roadmap.json).")


if __name__ == "__main__":
    build()
