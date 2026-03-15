import os
from config import DEFAULT_PROMPT
from orchestrator import MultiAgentOrchestrator

def main():
    if not os.path.exists("data/renewable_energy.db"):
        print("Database not found. Run: python3 init_db.py")
        return

    orchestrator = MultiAgentOrchestrator()
    result = orchestrator.run(DEFAULT_PROMPT)

    print("\n" + "=" * 80)
    print("PROMPT")
    print("=" * 80)
    print(result["prompt"])

    print("\n" + "=" * 80)
    print("PLANNER DECISION")
    print("=" * 80)
    print(result["plan"])

    print("\n" + "=" * 80)
    print("AGENT OUTPUTS")
    print("=" * 80)
    for item in result["agent_outputs"]:
        print(f"\n[{item['agent_name']}]")
        print(item["summary"])
        print("Evidence:")
        for ev in item["evidence"]:
            print(f"- {ev}")

    print("\n" + "=" * 80)
    print("FINAL SYNTHESIZED RESPONSE")
    print("=" * 80)
    print(result["final_response"])

if __name__ == "__main__":
    main()
