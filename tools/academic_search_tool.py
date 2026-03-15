import json
from config import ACADEMIC_DATA_PATH

def search_academic_papers(prompt: str) -> list[str]:
    with open(ACADEMIC_DATA_PATH, "r", encoding="utf-8") as file:
        papers = json.load(file)

    keywords = ["renewable", "energy", "environment", "economic", "europe", "grid", "storage"]
    matches = []

    for paper in papers:
        combined_text = (paper["title"] + " " + paper["summary"]).lower()
        if any(keyword in combined_text for keyword in keywords):
            matches.append(f"{paper['title']}: {paper['summary']}")

    return matches[:4]
