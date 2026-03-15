import json
import requests
from config import OLLAMA_MODEL, OLLAMA_URL, OLLAMA_TIMEOUT

def _call_ollama(system_prompt: str, user_prompt: str) -> str:
    prompt = f"System:\n{system_prompt}\n\nUser:\n{user_prompt}\n\nAssistant:"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=OLLAMA_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()

def ask_ollama_text(system_prompt: str, user_prompt: str) -> str:
    try:
        text = _call_ollama(system_prompt, user_prompt)
        if text:
            return text
        return "No response returned by Ollama."
    except Exception as e:
        return f"[LLM call failed] {e}"

def ask_ollama_json(system_prompt: str, user_prompt: str, fallback: dict) -> dict:
    try:
        text = _call_ollama(system_prompt, user_prompt)
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            parsed = json.loads(text[start:end+1])
            if isinstance(parsed, dict):
                return parsed
        return fallback
    except Exception:
        return fallback
