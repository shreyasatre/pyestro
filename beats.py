# https://scampsters.marcevanstein.com/t/the-beat-seems-erratic/467

import random
from scamp import *

s = Session(tempo=120)

drum_kits = ['TR 808', 'Power', 'Standard',]
drums = s.new_part(random.choice(drum_kits))

parts_to_midi = {
    "kick": 36,
    "snare": 38,
    "hihat": 42,
    "open_hihat": 46,
    "ride_cymbal": 51,
    "crash_cymbal": 49,
    "tom": 47,
    "tom_high": 45,
    "tom_mid": 43,
    "tom_low": 41,
    "clap":39,
}

beat = {
        'kick': [(1, 0.8),  (1, 0.0),  (1, 0.8),  (1, 0.0)], 
        'snare': [(1, 0.0), (1, 0.6), (1, 0.0), (1, 0.6)], 
        'hihat': [(0.5, 0.8), (0.5, 0.8),(0.5, 0.8),(0.5, 0.8),(0.5, 0.8),(0.5, 0.8),(0.5, 0.8),(0.5, 0.8)]}

def play_part(inst, part_name):
    this_part = beat[part_name]
    for b in this_part:
        inst.play_note(parts_to_midi[part_name], b[1], b[0])
        
count = 0
while count < 4:
    for part in list(beat.keys()):
        fork(play_part, args=(drums, part))
        
    wait_for_children_to_finish()
    count += 1