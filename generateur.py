import json
import numpy as np
from mido import Message, MidiFile, MidiTrack

def create_midi_file(notes,velocity,temps):
    track=MidiTrack()
    outfile=MidiFile()
    outfile.tracks.append(track)
    track.append(Message('program_change', program=12))

    for note in notes:
        track.append(Message('note_on', note=note+12*5, velocity=64, time=100))
        track.append(Message('note_off', note=note+12*5, velocity=127, time=100))
        #track.append(Message('note_on', note=note+12*5, velocity=int(velocity[str(note)]), time=int(temps[str(note)])))
        #track.append(Message('note_off', note=note+12*5, velocity=int(velocity[str(note)]), time=int(temps[str(note)])))

    outfile.save('test.mid')

def generate_music():
    with open('markov_model.json','r') as file:
        data=file.read()
    data=json.loads(data)
    A=data['A']
    pi=data['pi']
    vel=data['velocity']
    temps=data['temps']
    nb_notes=data['nb_notes']
    #nb_notes=10
    doublets=data['doublets']
    set_notes=list(range(12))+doublets
    print(set_notes)
    print(len(set_notes))
    is_doublet=False
    cs=np.cumsum(pi)
    a=np.random.rand(1)
    i=0
    while cs[i]<a:
        i+=1
    old_val=i
    res=[old_val]
    if old_val>=12:
        is_doublet=True
    for j in range(nb_notes-1):
        if is_doublet:
            is_doublet=False
            continue
        cs=np.cumsum(A[old_val])
        a=np.random.rand(1)
        i=0
        while cs[i]<a:
            i+=1
        old_val=i
        if old_val>=12:
            is_doublet=True
        res.append(old_val)

    #print(res)
    with_doublet=[]
    for item in res:
        if item<12:
            with_doublet.append(item)
        else:
            with_doublet.append(set_notes[item][0])
            with_doublet.append(set_notes[item][1])
    #print(with_doublet)
    print(type(vel))
    print(type(temps))
    create_midi_file(with_doublet,vel,temps)
generate_music()