import json
from config import RECOMMENDATION_DATA_PATH

def get_recommendations(prompt: str) -> list[str]:
    with open(RECOMMENDATION_DATA_PATH, "r", encoding="utf-8") as file:
        items = json.load(file)

    return [f"{item['title']}: {item['description']}" for item in items[:4]]
