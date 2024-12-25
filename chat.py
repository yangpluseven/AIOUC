import requests
import json
from constants import *


def generate_using_model(prompt, model="llama3.1", num_predict=2048):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": num_predict},
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        try:
            lines = response.text.strip().split("\n")
            last_response = json.loads(lines[-1])
            return last_response.get("response", "null")
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code}"


def chat_with_model(prompt, model="llama3.1", num_predict=2048):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"num_predict": num_predict},
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        try:
            lines = response.text.strip().split("\n")
            last_response = json.loads(lines[-1])
            return last_response.get("message", {}).get("content", "null")
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code}"


def generate_decision(response, model="llama3.1", num_predict=2048):
    response = (
        "Based on the monologues above:\n"
        + response
        + "\nPlease Return a JASON object that contains his coin allocation array.\n"
    )
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": response,
        "stream": False,
        "format": {
            "type": "object",
            "properties": {
                "coins allocated": {"type": "array", "items": {"type": "number"}},
            },
        },
        "options": {"num_predict": num_predict},
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        try:
            lines = response.text.strip().split("\n")
            last_response = json.loads(lines[-1])
            return last_response.get("response", "null")
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code}"


def chat_decision(response, model="llama3.1", num_predict=2048):
    response = (
        "Based on the monologues above:\n"
        + response
        + "\nPlease Return a JASON object that contains his final coin allocation array.\n"
    )
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": response}],
        "stream": False,
        "format": {
            "type": "object",
            "properties": {
                "coins allocated": {"type": "array", "items": {"type": "number"}},
            },
        },
        "options": {"num_predict": num_predict},
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        try:
            lines = response.text.strip().split("\n")
            last_response = json.loads(lines[-1])
            return last_response.get("message", {}).get("content", "null")
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code}"


if __name__ == "__main__":
    response = chat_with_model(TEST_PROMPT_FOUR, num_predict=500)
    print(response)
    response = chat_decision(response, num_predict=50)
    print(response)
    parsed_json = json.loads(response)
    print(parsed_json)
