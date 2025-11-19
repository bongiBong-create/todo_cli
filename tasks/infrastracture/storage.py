import json
from pathlib import Path

def init_path(file="data.json"):
    current_path = Path(__file__).parent/file
    return current_path

def init_storage(file_path):
    path = Path(file_path)
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_tasks(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)

def save_category(file_path, category):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(category, f, ensure_ascii=False)

def load_category(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)