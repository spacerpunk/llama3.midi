import requests
import json
import mingus.core.notes as notes
import mido
from mido import Message

model = 'llama3.2:latest'
messages = []
# Roles
USER = 'user'
ASSISTANT = 'assistant'

# API endpoint
url = "http://localhost:11434/api/chat"

# PROMPT
constant =  "You are a helpful agent that only responds with a single JSON object for MIDI. Do not provide explanations or other text outside of the JSON object. If you need to provide an explanation, generate an appropriate response in JSON format. "
example = "the exact response of the JSON File shoud be in this format [{'event':'note_on', 'note':'60', 'velocity':64, 'time':0.5}]. "
end = "Please respond with only a single JSON object and no additional text."
#prompt = input('Prompt: ')
prompt = "give a midi file in C Major, with note_on, note_off, note, duration and velocity data, 40 notes"

# Request payload
payload = {
    "model": "llama3.2:latest",
    # "format":"json",
    "messages": [
        {"role": "user", 
        "content": "hello!"} #constant + example + prompt + end
    ],
    "stream": False,
    "temperature": 0,
    "n_context": 8000,
    "seed": 4815162342
}

# Send POST request
response = requests.post(url, json=payload)

# Get response
result = response.json()
midi_json = json.loads(result["message"])
print(midi_json)

def add_history(content, role):
    messages.append({'role': role, 'content': content})

# Play the sequence of notes
# def playMidi(event,note,velocity,time):
#     message = Message(event, note=note, velocity=int(velocity), time=int(time))
#     print(message)
#     #port.send(message)

# index = 0
# for n in midi_json:
#     event = midi_json[index]["event"]
#     note = midi_json[index]["note"]
#     velocity = midi_json[index]["velocity"]
#     time = midi_json[index]["time"] 

#     playMidi(event,note,velocity,time)
#     index += 1
#     print(index)

#     #print(midi_json)
#     #print(event)
#     #print(note)
#     #print(velocity)
#     #print(time)


