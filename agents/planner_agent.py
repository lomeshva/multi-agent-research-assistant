import json
from utils.llm import ask_ollama_json

class PlannerAgent:
    def run(self, prompt: str) -> dict:
        system_prompt = (
            "You are a planner agent in a multi-agent research system. "
            "Choose which agents should run for the user's question. "
            "Valid agent names are: economic, academic, news, recommendation. "
            "Return valid JSON only with keys selected_agents and planner_notes. "
            "selected_agents must be a JSON array of strings."
        )

        user_prompt = f"User question: {prompt}"

        fallback = {
            "selected_agents": ["economic", "academic", "news", "recommendation"],
            "planner_notes": "The question asks for both economic and environmental impacts, so all agents are useful."
        }

        data = ask_ollama_json(system_prompt, user_prompt, fallback=fallback)

        selected = data.get("selected_agents", [])
        if not isinstance(selected, list):
            selected = fallback["selected_agents"]

        planner_notes = data.get("planner_notes", fallback["planner_notes"])

        return {
            "selected_agents": selected,
            "planner_notes": planner_notes,
            "raw_plan_text": json.dumps(
                {
                    "selected_agents": selected,
                    "planner_notes": planner_notes
                },
                indent=2
            )
        }
