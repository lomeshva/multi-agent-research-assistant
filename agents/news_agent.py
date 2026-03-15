from tools.news_search_tool import search_recent_news
from utils.llm import ask_ollama_text

class NewsAgent:
    def run(self, prompt: str) -> dict:
        news_items = search_recent_news(prompt)

        system_prompt = (
    "You are the News Agent in a multi-agent research assistant. "
    "You receive recent policy and news-style updates related to renewable energy in Europe. "
    "Write one concise paragraph using only the provided evidence. "
    "Do not add projections, statistics, or claims that are not explicitly stated in the evidence. "
    "If the evidence does not mention a number, do not invent one."
)

        user_prompt = f'''
User question: {prompt}

Policy/news findings:
{chr(10).join("- " + n for n in news_items)}
'''

        summary = ask_ollama_text(system_prompt, user_prompt)

        return {
            "agent_name": "News Agent",
            "summary": summary,
            "evidence": news_items
        }
