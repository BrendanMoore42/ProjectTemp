import glob
import pickle
import mido


def get_notes():
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    notes = []

    for file in glob.glob("C:/Users/B/Desktop/midis/Nintendo/Nintendo/DKR/*.mid"):
        midi = converter.parse(file)

        print("Parsing %s" % file)

        notes_to_parse = None

        try: # file has instrument parts
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        except: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    with open('C:/Users/B/Desktop/midis/data/notes.pkl', 'wb') as filepath:
        pickle.dump(notes, filepath)

    return notes

get_notes()

# with open('C:/Users/B/Desktop/midis/data/notes.pkl', 'rb') as f:
#     file = pickle.load(f)
# print(file)