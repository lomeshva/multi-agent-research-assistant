from tools.academic_search_tool import search_academic_papers
from utils.llm import ask_ollama_text

class AcademicAgent:
    def run(self, prompt: str) -> dict:
        papers = search_academic_papers(prompt)

        system_prompt = (
    "You are the Academic Agent in a multi-agent research assistant. "
    "You receive research-style findings about renewable energy adoption in Europe. "
    "Write one concise paragraph summarizing the literature. "
    "Use only the provided findings. "
    "Do not introduce extra claims beyond the evidence."
)

        user_prompt = f'''
User question: {prompt}

Academic findings:
{chr(10).join("- " + p for p in papers)}
'''

        summary = ask_ollama_text(system_prompt, user_prompt)

        return {
            "agent_name": "Academic Agent",
            "summary": summary,
            "evidence": papers
        }
