import datetime
import json
from typing import Dict, List


def get_all_message() -> List[Dict]:
    with open("chat_history.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def add_message(content, color):
    messages.append(
        {
            "content": content,
            "color": color,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f)


messages = get_all_message()
