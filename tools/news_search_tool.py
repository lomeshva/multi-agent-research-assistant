import json
from config import NEWS_DATA_PATH

def search_recent_news(prompt: str) -> list[str]:
    with open(NEWS_DATA_PATH, "r", encoding="utf-8") as file:
        items = json.load(file)

    keywords = ["renewable", "energy", "europe", "policy", "solar", "wind", "grid"]
    matches = []

    for item in items:
        combined_text = (item["headline"] + " " + item["summary"]).lower()
        if any(keyword in combined_text for keyword in keywords):
            matches.append(f"{item['headline']}: {item['summary']}")

    return matches[:4]
