import datetime
import json
import uuid
from typing import Dict


def get_all_message() -> Dict:
    with open("chat_history.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def add_message(content, color):
    messages[uuid.uuid4().hex] = {
        "content": content,
        "color": color,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f)


messages = get_all_message()
