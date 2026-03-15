from pydantic import BaseModel
from typing import List

class AgentResult(BaseModel):
    agent_name: str
    summary: str
    evidence: List[str]
