# https://scampsters.marcevanstein.com/t/are-note-names-supported-in-scamp/169
# https://scampsters.marcevanstein.com/t/c4-d4-e4-rather-than-60-62-64/419

named_notes = {
    f"{letter}{alteration}{octave}": [9, 11, 12, 14, 16, 17, 19]["ABCDEFG".index(letter.upper())] + \
    12 * octave + [-1, 0, 1][("b", "", "#").index(alteration)]
    for letter in "ABCDEFGabcdefg"
    for alteration in ("b", "", "#")
    for octave in range(0, 9)
}

named_notes = {
    f"{letter}{alteration}{octave}": [12, 14, 16, 17, 19, 21, 23, 24]["CDEFGAB".index(letter.upper())] + \
    12 * octave + [-1, 0, 1][("b", "", "#").index(alteration)]
    for letter in "ABCDEFGabcdefg"
    for alteration in ("b", "", "#")
    for octave in range(0, 9)
}

print("with dictionary comprehension")
print(named_notes["c4"])
print(named_notes["D#5"])
print(named_notes["Eb3"])

print()

pitch_class_displacements = {
    'c': 0,
    'd': 2,
    'e': 4,
    'f': 5,
    'g': 7,
    'a': 9,
    'b': 11
}

accidental_displacements = {
    '#': 1,
    's': 1,
    'f': -1,
    'b': -1,
    'x': 2,
    'bb': -2
}

def note_name_to_number(note_name: str):
    note_name = note_name.lower().replace(' ', '')
    pitch_class_name = note_name[0]
    octave = note_name[-1]
    accidental = note_name[1:-1]
    return (int(octave) + 1) * 12 + \
           pitch_class_displacements[pitch_class_name] + \
           (accidental_displacements[accidental] if accidental in accidental_displacements else 0)


print("without dictionary comprehension")
print(note_name_to_number("c4"))
print(note_name_to_number("fs5"))
print(note_name_to_number("bf3"))

# srgmpdn
# cdefgab