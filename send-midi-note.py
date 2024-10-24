import time
import random
import mido
from mido import Message, MidiFile, MidiTrack
import mingus
import mingus.core.notes as notes
import mingus.core.scales as scales
from mingus.containers import Note

# inputs = mido.get_input_names()
# outputs = mido.get_output_names()

# print('inputs: ', inputs)
# print('outputs: ', outputs)

# select a MIDI input port by name
# input_port = mido.open_input('Keystation 88 1')

# create a MIDI out port
midi_out = mido.open_output("loopMIDI Port 1")
#midi_out_2 = mido.open_output("Python Out 4")

bpm = 60 / 100

#Defines Scales
notes = ["C", "D", "E", "F", "G", "A", "B"]
print(notes[random.randrange(0,len(notes))])

#Old Midi Notes
cMajor = [60, 62, 64, 65, 67, 69, 71, 72]

ionian = scales.Ionian(notes[random.randrange(0,len(notes))])
aeolian = scales.Aeolian(notes[random.randrange(0,len(notes))])
naturalMinor = scales.NaturalMinor(notes[random.randrange(0,len(notes))])
scales = [ionian, aeolian, naturalMinor]

#Creates Empty Array         
notesArray = []

#Convert Mingus Notation to Midi Notation using the "Notes Class" and stores the new midi notes in the empty array
def convertNotes():
    scale = scales[random.randrange(0,len(scales))]
    scale = naturalMinor
    print(scale)
    for note in scale.ascending():
        n = int(Note(note, random.randrange(4,5)))
        notesArray.append(n)
        
convertNotes()
print(notesArray)

#Generates Midi Notes and Sends it out
def noteGenerator(velocity, velocity2):
    note = notesArray[random.randrange(0,len(notesArray))]
    note2 = notesArray[random.randrange(0,len(notesArray))]
    #print(note)
    note_one = Message('note_on', note=note, velocity=velocity)
    note_two = Message('note_on', note=note2, velocity=velocity2)
    midi_out.send(note_one)
    midi_out.send(note_two)
    # time.sleep(bpm / random.randrange(1,4))
    time.sleep(bpm * 4)
    note_one_off = Message('note_off', note=note, velocity=0)
    note_two_off = Message('note_off', note=note2, velocity=0)
    midi_out.send(note_one_off)
    midi_out.send(note_two_off)
    
#Sequences Midi Notes
def sequenceGenerator(numberOfNotes):    
    for a in range(numberOfNotes):
        noteGenerator(random.randrange(35,100),random.randrange(30,80))
    #sequenceGenerator(numberOfNotes)
        
sequenceGenerator(10)    

# # loop to receive MIDI messages
# for message in input_port:
#     print(message)
#     sequenceGenerator(2)

# close the MIDI out port
midi_out.close()


