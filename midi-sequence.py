import mingus.core.notes as notes
import mido
from mido import Message
import requests
import json

inputs = mido.get_input_names()
outputs = mido.get_output_names()
url = "http://localhost:11434/api/chat"
prompt = 'I need you to give me a midi sequence of notes in a Python Dictionary in this exact format, ONLY give me the Dictionary { "track": [ {"event_type": "note_on", "time": 0, "note": 60, "velocity": 64} ]'

track = [{"event_type": "note_on", "time": 0, "note": 60, "velocity": 64},
        {"event_type": "note_off", "time": 1000, "note": 60, "velocity": 0},
        {"event_type": "note_on", "time": 2000, "note": 62, "velocity": 64},
        {"event_type": "note_off", "time": 3000, "note": 62, "velocity": 0},
        {"event_type": "note_on", "time": 4000, "note": 64, "velocity": 64},
        {"event_type": "note_off", "time": 5000, "note": 64, "velocity": 0},
        {"event_type": "note_on", "time": 6000, "note": 67, "velocity": 64},
        {"event_type": "note_off", "time": 7000, "note": 67, "velocity": 0},
        {"event_type": "note_on", "time": 8000, "note": 69, "velocity": 64},
        {"event_type": "note_off", "time": 9000, "note": 69, "velocity": 0}
    ]

print(type(track))
print(type(track[0]))
# print('inputs: ', inputs)
# print('outputs: ', outputs)


# Define the MIDI output port
# port = mido.open_output("loopMIDI Port 1")
# print(port)

# Define a sequence of note names
note_names = ["C", "D", "E", "F", "G", "A", "B", "C"]

# Convert the note names to MIDI numbers
notes = [notes.note_to_int(note) for note in note_names]

def llamaMessage(prompt):
    payload = {
        "model": "llama3.2:latest",
        "messages": [
            {"role": "user", 
            "content": prompt}
        ],
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    return result

def midiDict(result):
    print(result["message"]["content"])

num = 0
for a in range(10):
    print(num)
    num += 1

# Simple iteration
for event in track:
    print(event)

# With index
for i, event in enumerate(track):
    print(f"Event {i}: {event}")

# Print specific values
for event in track:
    print(f"Type: {event['event_type']}, Note: {event['note']}, Time: {event['time']}")

#parseMidi(llamaMessage(prompt))

# Play the sequence of notes
# for a in track:
#     message = Message(track[0]["event_type"], note=track[], velocity=track["track"][0]["velocity"], time=track["track"][0]["time"])
#     print(message)
#     port.send(message)

# # Close the MIDI output port
# port.close()

