import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "users.json"

def load_users() -> dict:
    if not DATA_PATH.exists():
        return {}
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_users(users: dict) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def get_user(users: dict, user_id: int) -> dict:
    key = str(user_id)
    if key not in users:
        users[key] = {"quiz_done": 0, "quiz_score": 0}
    return users[key]
