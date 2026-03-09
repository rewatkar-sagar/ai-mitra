import requests
import json

def analyze_text(user_text):
    """
    Analyzes text for scams or misinformation using local Ollama (Llama 3).
    This function expects Ollama to be running locally on port 11434.
    """
    url = "http://localhost:11434/api/generate"

    # We instruct Llama 3 to act as AI Mitra and return strict JSON.
    prompt = f"""
    You are AI Mitra, an AI safety assistant. Analyze the following message for scams, phishing, or misinformation.
    Message: "{user_text}"

    Return ONLY a JSON object with the following exact keys:
    - "risk_level": (String) Must be "Low", "Medium", or "High"
    - "explanation": (String) A brief, easy-to-understand explanation of the risk
    - "verification_tip": (String) Actionable advice on how the user can verify this information
    """

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "format": "json"  # Forces Ollama to output valid JSON
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        # The actual text response from Llama 3 is inside the 'response' key
        result_text = data.get("response", "{}")
        
        # Parse the stringified JSON from the LLM into a Python dictionary
        return json.loads(result_text)
        
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: Is Ollama running? {e}")
        return {
            "risk_level": "Unknown",
            "explanation": "Could not connect to the local AI engine. Please ensure Ollama is running.",
            "verification_tip": "Check your backend server logs."
        }
    except json.JSONDecodeError:
        print("JSON Parsing Error: The model did not return valid JSON.")
        return {
            "risk_level": "Unknown",
            "explanation": "The AI provided an unreadable response.",
            "verification_tip": "Try analyzing the message again."
        }