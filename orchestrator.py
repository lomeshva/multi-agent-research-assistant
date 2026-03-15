from agents.planner_agent import PlannerAgent
from agents.economic_agent import EconomicAgent
from agents.academic_agent import AcademicAgent
from agents.news_agent import NewsAgent
from agents.recommendation_agent import RecommendationAgent
from agents.final_synthesizer import FinalSynthesizer

class MultiAgentOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.economic_agent = EconomicAgent()
        self.academic_agent = AcademicAgent()
        self.news_agent = NewsAgent()
        self.recommendation_agent = RecommendationAgent()
        self.final_synthesizer = FinalSynthesizer()

    def run(self, prompt: str) -> dict:
        plan = self.planner.run(prompt)

        selected = set(plan["selected_agents"])
        agent_outputs = []

        if "economic" in selected:
            agent_outputs.append(self.economic_agent.run(prompt))
        if "academic" in selected:
            agent_outputs.append(self.academic_agent.run(prompt))
        if "news" in selected:
            agent_outputs.append(self.news_agent.run(prompt))
        if "recommendation" in selected:
            agent_outputs.append(self.recommendation_agent.run(prompt))

        if not agent_outputs:
            agent_outputs.append(self.economic_agent.run(prompt))
            agent_outputs.append(self.academic_agent.run(prompt))
            agent_outputs.append(self.news_agent.run(prompt))
            agent_outputs.append(self.recommendation_agent.run(prompt))

        final_response = self.final_synthesizer.run(prompt, plan["planner_notes"], agent_outputs)

        return {
            "prompt": prompt,
            "plan": plan["raw_plan_text"],
            "agent_outputs": agent_outputs,
            "final_response": final_response
        }
