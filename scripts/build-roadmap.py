import json
import os

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def build():
    roadmap = {
        "vision": load_json('data/roadmap/vision.json'),
        "pillars": load_json('data/roadmap/pillars.json'),
        "programs": load_json('data/roadmap/programs.json'),
        "projects": load_json('data/roadmap/projects.json'),
        "milestones": load_json('data/roadmap/milestones.json'),
        "tasks": load_json('data/roadmap/tasks.json'),
        "movedLater": load_json('data/roadmap/moved_later.json'),
        "looseThreads": load_json('data/roadmap/loose_threads.json'),
        "conflicts": load_json('data/roadmap/conflicts.json')
    }
    
    with open('roadmap.json', 'w') as f:
        json.dump(roadmap, f, indent=2)
    print("✅ Roadmap compiled to roadmap.json")

if __name__ == "__main__":
    build()
