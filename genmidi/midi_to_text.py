"""
author: @BrendanMoore42
date: November 30, 2018

Converts a Midi file to text. And perhaps back again.
"""
# import textgenrnn
import py_midicsv as mc
# Load midi file
midi = mc.midi_to_csv("C:/Users/B/Desktop/midis/Nintendo/DKR/DKRDrago.mid")

print(midi.readlines())


# Parse the CSV output of the previous command back into a MIDI file
midi_object = mc.csv_to_midi(midi)

# Save the parsed MIDI file to disk
with open("example_converted.mid", "wb") as output_file:
    midi_writer = mc.FileWriter(output_file)
    midi_writer.write(midi_object)

