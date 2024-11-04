import random
import requests
import json
import mingus.core.notes as notes
import mido
from mido import Message
import time

USER = 'user'
ASSISTANT = 'assistant'
model = 'llama3.2:latest'
bpm = 60

# PROMPT
constant =  "You are a helpful agent that only responds with a single JSON object for MIDI. Do not provide explanations or other text outside of the JSON object. If you need to provide an explanation, generate an appropriate response in JSON format. "
example = "the exact response of the JSON File shoud be in this format [{'event':event_value, 'note':note_value, 'velocity':velocity_value, 'time':0.5}], Velocity should be within 0 and 127 and always be an integer number, not always the same number. "
end = "Please respond with only a single JSON object with note_on, note_off, note, duration and velocity data, 50 notes and no additional text."
#prompt = input('Prompt: ')
prompt = "give a midi file in D Minor, "

messages = [
        {
            "role": "user",
            "content": constant + example + prompt + end,
            #"content": "Hello, what is your name?"
        }
    ]

# API endpoint
url = "http://localhost:11434/api/chat"

# Request payload
payload = {
    "model": model,
    "messages": messages,
    "options": {
        "seed": 4815162342,
        "temperature": 0.1
    },
    "stream": False,
    
}

# Send POST request
response = requests.post(url, json=payload)

# Get response
result = response.json()
midi_json = json.loads(result["message"]["content"])
print(result["message"]["content"])
#print(type(result["message"]["content"]))
#print(midi_json)
#print(midi_json[0]["event"])


def add_history(content, role):
    messages.append({'role': role, 'content': content})

# MIDI PART #
inputs = mido.get_input_names()
outputs = mido.get_output_names()

print('inputs: ', inputs)
print('outputs: ', outputs)

# create a MIDI out port
midi_out = mido.open_output("Python 1")

# Play the sequence of notes
def playMidi(event,note,velocity,time):
    message = Message(event, note=note, velocity=int(velocity), time=int(time))
    print(message)
    #port.send(message)

# Generates Midi Notes and Sends it out
def noteGenerator(velocity, note, tiempo):
    #note = notesArray[random.randrange(0,len(notesArray))]
    #print(note)
    note_one = Message('note_on', note=note, velocity=velocity)
    midi_out.send(note_one)
    #time.sleep(bpm / random.randrange(1,4))
    time.sleep(tiempo)
    note_off = Message('note_off', note=note, velocity=0)
    midi_out.send(note_off)
    #time.sleep(random.randrange(0,1))
    


print(type(midi_json[0]["note"]))
print(type(midi_json[0]["velocity"]))

# MAKE THIS AND THE CHAT PAYLOAD A FUNCTION 
# TO MAKE IT A GRADIO APP
index = 0
for n in midi_json:
    llama_event = midi_json[index]["event"]
    llama_note = int(midi_json[index]["note"])
    llama_velocity = midi_json[index]["velocity"]
    llama_time = midi_json[index]["time"]
    noteGenerator(llama_velocity, llama_note, llama_time)
    index += 1
    print(f"Index: {index}, Note: {llama_note}, Velocity: {llama_velocity}, Time: {llama_time}")