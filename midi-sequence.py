import mingus.core.notes as notes
import mido
from mido import Message

inputs = mido.get_input_names()
outputs = mido.get_output_names()

print('inputs: ', inputs)
print('outputs: ', outputs)


# Define the MIDI output port
port = mido.open_output("loopMIDI Port 1")
#print(port)

# Define a sequence of note names
note_names = ["C", "D", "E", "F", "G", "A", "B", "C"]

# Convert the note names to MIDI numbers
notes = [notes.note_to_int(note) for note in note_names]

# Play the sequence of notes
for note in notes:
    message = Message('note_on', note=note, velocity=64, time=0.5)
    print(message)
    port.send(message)

# Close the MIDI output port
port.close()

