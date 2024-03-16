from scamp import *
from enum import Enum

s = Session()

# s.print_default_soundfont_presets()

class Sargam(Enum):
    SA = 60
    RE = 62
    GA = 64
    MA = 65
    PA = 67
    DH = 69
    NI = 71
    SAA = 72

# PA SA RE GA SA RE SA NI DH NI PA DH NI SA RE GA SA RE NI SA
# 1.0 1.0 1.0 1.0

flute_gold = s.new_part("Flute Gold")
# flute_pan = s.new_part("Pan Flute")
# glockenspiel = s.new_part("Glockenspiel")

notes_list = [Sargam.SA.value, Sargam.RE.value, Sargam.GA.value, Sargam.MA.value, Sargam.PA.value, Sargam.DH.value, Sargam.NI.value, Sargam.SAA.value]
durs_list = [1.0] * len(notes_list)

for note, duration in zip(notes_list, durs_list):
    flute_gold.play_note(note, 0.5, duration)

