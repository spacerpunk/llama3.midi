import random
import requests
import json
import mingus.core.notes as notes
import mido
from mido import Message
import time

####### LLAMA SETUP #######
USER = 'user'
ASSISTANT = 'assistant'
model = 'llama3.2:latest'
bpm = 60 / 100

constant =  "You are a helpful agent that only responds with a single JSON object for MIDI. Do not provide explanations or other text outside of the JSON object. If you need to provide an explanation, generate an appropriate response in JSON format. "
example = "the exact response of the JSON File shoud be in this format [{'event':'note_on', 'note':'60', 'velocity':64, 'time':0.5}], Velocity should be within 0 and 127 and always be an integer number, not always the same number. "
end = "Please respond with only a single JSON object and no additional text."
#prompt = input('Prompt: ')
prompt = "give a midi file in C Major, with note_on, note_off, note, duration and velocity data, 40 notes"

messages = [
        {
            "role": "user",
            "content": constant + example + prompt + end,
            #"content": "Hello, what is your name?"
        }
    ]

# API endpoint
url = "http://localhost:11434/api/chat"


####### MIDI SETUP #######
inputs = mido.get_input_names()
outputs = mido.get_output_names()

print('inputs: ', inputs)
print('outputs: ', outputs)

# create a MIDI out port
midi_out = mido.open_output("loopMIDI Port 2")

#SENDS THE REQUEST AND GETS THE RESPONSE FROM LLAMA3
def chat(messages):
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
    return midi_json


def add_history(content, role):
    messages.append({'role': role, 'content': content})

# Generates Midi Notes and Sends it out
def noteGenerator(velocity, note, tiempo):
    #note = notesArray[random.randrange(0,len(notesArray))]
    #print(note)
    note_one = Message('note_on', note=note, velocity=velocity)
    midi_out.send(note_one)
    # time.sleep(bpm / random.randrange(1,4))
    time.sleep(tiempo * random.randrange(0,5))
    note_off = Message('note_off', note=note, velocity=0)
    midi_out.send(note_off)
    time.sleep(random.randrange(0,1))
    


#MAKE THIS AND THE CHAT PAYLOAD A FUNCTION SO WE CAN RECURSIVELY CALL IT

# Play the sequence of notes
def playMidi():
    midi_json = chat(messages)
    add_history()

    index = 0
    for n in midi_json:
        llama_event = midi_json[index]["event"]
        llama_note = int(midi_json[index]["note"])
        llama_velocity = midi_json[index]["velocity"]
        llama_time = midi_json[index]["time"]
        noteGenerator(llama_velocity, llama_note, llama_time)
        index += 1
        print(f"Index: {index}, Note: {llama_note}, Velocity: {llama_velocity}, Time: {llama_time}")
    