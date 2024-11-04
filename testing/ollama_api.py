import ollama

# PROMPT
constant =  "You are a helpful agent that only responds with a single JSON object for MIDI. Do not provide explanations or other text outside of the JSON object. If you need to provide an explanation, generate an appropriate response in JSON format. "
example = "the exact response of the JSON File shoud be in this format [{'event':'note_on', 'note':'60', 'velocity':64, 'time':0.5}]. "
end = "Please respond with only a single JSON object and no additional text."
#prompt = input('Prompt: ')
prompt = "give a midi file in C Major, with note_on, note_off, note, duration and velocity data, 40 notes"

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "What is einstein know for?",
        },
    ],
)

print(response["message"]["content"])