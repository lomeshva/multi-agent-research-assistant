# Multi-Agent Research Assistant (Ollama Version)

This is a more realistic multi-agent system that uses **Ollama** for LLM-based planning, agent reasoning, and final synthesis.

## What makes this version more agentic?

This version does **not** just return fixed strings.

It uses:
- a **Planner Agent** that asks the LLM which agents should run
- specialized agents that call tools and then ask the LLM to interpret the tool output
- a **Final Synthesizer Agent** that asks the LLM to combine all agent results into one final answer
- a SQLite database for structured economic data
- local JSON knowledge bases for academic papers, news, and recommendations

## Architecture

User Prompt
-> Planner Agent (LLM decides which agents to call)
-> Economic Agent (SQL tool + LLM summary)
-> Academic Agent (search tool + LLM summary)
-> News Agent (search tool + LLM summary)
-> Recommendation Agent (recommendation tool + LLM summary)
-> Final Synthesizer (LLM combines all agent outputs)

## Project Structure

```text
multi_agent_research_assistant_ollama/
├── agents/
│   ├── __init__.py
│   ├── academic_agent.py
│   ├── economic_agent.py
│   ├── final_synthesizer.py
│   ├── news_agent.py
│   ├── planner_agent.py
│   └── recommendation_agent.py
├── data/
│   ├── academic_papers.json
│   ├── news_updates.json
│   ├── recommendations.json
│   └── renewable_energy.db
├── tools/
│   ├── __init__.py
│   ├── academic_search_tool.py
│   ├── news_search_tool.py
│   ├── recommendation_tool.py
│   └── sql_tool.py
├── utils/
│   ├── __init__.py
│   ├── db.py
│   ├── llm.py
│   └── models.py
├── config.py
├── init_db.py
├── main.py
├── orchestrator.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Make sure Ollama is installed
Install Ollama on your machine first.

### 2. Pull a model
Example:
```bash
ollama pull llama3.1:8b
```

You can also use `mistral`, `qwen2.5`, etc.

### 3. Create a virtual environment
```bash
python3 -m venv .venv
```

### 4. Activate it
```bash
source .venv/bin/activate
```

### 5. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 6. Initialize the database
```bash
python3 init_db.py
```

### 7. Run the system
```bash
python3 main.py
```

## If Python on your Mac only works inside the venv
```bash
./.venv/bin/python init_db.py
./.venv/bin/python main.py
```

## Configure the Ollama model

Edit `config.py` if needed:

```python
OLLAMA_MODEL = "llama3.1:8b"
OLLAMA_URL = "http://localhost:11434/api/generate"
```

## Important note

The academic/news search in this project is still local and simple, but the reasoning, planning, and synthesis are LLM-driven through Ollama.

That makes it much closer to a real agent system than the earlier fixed-output version.
