import ollama

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Give me a JSON of a Midi file of 5 notes playing in C major",
        },
    ],
)
print(response["message"]["content"])