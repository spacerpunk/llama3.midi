import requests
import json

# API endpoint
url = "http://localhost:11434/api/chat"

# Request payload
payload = {
    "model": "llama3.2:latest",
    "messages": [
        {"role": "user", "content": "What are God Particles?"}
    ],
    "stream": False
}

# Send POST request
response = requests.post(url, json=payload)

# Get response
result = response.json()
print(result["message"]["content"])