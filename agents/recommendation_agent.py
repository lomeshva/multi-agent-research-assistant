from tools.recommendation_tool import get_recommendations
from utils.llm import ask_ollama_text

class RecommendationAgent:
    def run(self, prompt: str) -> dict:
        recommendations = get_recommendations(prompt)

        system_prompt = (
            "You are the Recommendation Agent in a multi-agent research assistant. "
            "You receive suggested reports and expert sources. "
            "Write a concise paragraph explaining why these sources are useful follow-up material."
        )

        user_prompt = f'''
User question: {prompt}

Recommended follow-up sources:
{chr(10).join("- " + r for r in recommendations)}
'''

        summary = ask_ollama_text(system_prompt, user_prompt)

        return {
            "agent_name": "Recommendation Agent",
            "summary": summary,
            "evidence": recommendations
        }
