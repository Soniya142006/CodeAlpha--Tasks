import glob
from music21 import converter, instrument, note, chord
import numpy as np

def get_notes():
    notes = []
    # Load all midi files in your directory
    for file in glob.glob("midi_songs/*.mid"):
        midi = converter.parse(file)
        notes_to_parse = None

        parts = instrument.partitionByInstrument(midi)
        if parts: # file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes

# Prepare sequences for training
def prepare_sequences(notes, n_vocab):
    sequence_length = 100
    pitchnames = sorted(set(item for item in notes))
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_length):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
        network_output.append(note_to_int[sequence_out])

    n_patterns = len(network_input)
    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(n_vocab) # Normalize

    return (network_input, network_output)
