from utils.llm import ask_ollama_text

class FinalSynthesizer:
    def run(self, prompt: str, planner_notes: str, agent_outputs: list[dict]) -> str:
        formatted_outputs = []

        for item in agent_outputs:
            block = (
                f"Agent: {item['agent_name']}\n"
                f"Summary: {item['summary']}\n"
                f"Evidence:\n" + "\n".join(f"- {ev}" for ev in item["evidence"])
            )
            formatted_outputs.append(block)

        system_prompt = (
    "You are the final synthesis agent in a multi-agent research assistant. "
    "Combine the planner notes and agent outputs into one coherent final response. "
    "Use only the evidence and summaries provided. "
    "Do not introduce new facts, projections, or numerical claims. "
    "If a detail is not supported by the evidence, do not mention it."
        )

        user_prompt = f'''
User question: {prompt}

Planner notes:
{planner_notes}

Agent outputs:
{chr(10).join(formatted_outputs)}
'''

        return ask_ollama_text(system_prompt, user_prompt)
