"""
author: @BrendanMoore42
date: November 30, 2018

Converts a Midi file to text. And perhaps back again.
"""
import sys
from mido import MidiFile
# from textgenrnn import textgenrnn

mid = MidiFile("C:/Users/B/Desktop/midis/Nintendo/DKR/Hauntedwoods.mid")
temp_midi = []

def grab_num_values(midi_string):
    '''
    Puts the numerical value to a dictionary.
    :param midi_string:
    :return:
    '''
    pass

for track in mid.tracks:

    print(track)

    # file = open('midi_txt_test1.txt', 'w+')
    for msg in track:

        # temp_midi.append(str(msg))
        print(msg)

print(mid.length)


# # with open('midi_txt_test1.txt', 'w') as f:
# #     f.writelines(temp_midi)
#
# # textgen = textgenrnn()
# #
# # # textgen.train_from_file
# # textgen.generate(string)
# print('\n\n\n\n', track)

# import py_midicsv as mc
# # Load midi file
# midi = mc.midi_to_csv("C:/Users/B/Desktop/midis/Nintendo/DKR/DKRDrago.mid")
#
# print(midi.readlines())
#
#
# # Parse the CSV output of the previous command back into a MIDI file
# midi_object = mc.csv_to_midi(midi)
#
# # Save the parsed MIDI file to disk
# with open("example_converted.mid", "wb") as output_file:
#     midi_writer = mc.FileWriter(output_file)
#     midi_writer.write(midi_object)
#
