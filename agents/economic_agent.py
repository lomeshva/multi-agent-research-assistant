from tools.sql_tool import get_economic_summary_from_db
from utils.llm import ask_ollama_text

class EconomicAgent:
    def run(self, prompt: str) -> dict:
        tool_output = get_economic_summary_from_db()

        system_prompt = (
            "You are the Economic Agent in a multi-agent research assistant. "
            "You receive structured database results about renewable energy adoption in Europe. "
            "Write one concise paragraph explaining the meaning of the numbers. "
            "Use only the provided database results. "
            "Do not add facts or estimates that are not explicitly present."
        )

        user_prompt = f'''
User question: {prompt}

Structured database results:
{tool_output}
'''

        summary = ask_ollama_text(system_prompt, user_prompt)

        evidence = [
            f"Average renewable share across sampled countries: {tool_output['avg_renewable_share']:.1f}%",
            f"Average greenhouse-gas reduction across sampled countries: {tool_output['avg_ghg_reduction']:.1f}%",
            f"Total jobs supported across sampled countries: {tool_output['total_jobs']:,}",
            f"Total renewable-energy investment across sampled countries: EUR {tool_output['total_investment']:.1f} billion",
        ]

        return {
            "agent_name": "Economic Agent",
            "summary": summary,
            "evidence": evidence
        }
