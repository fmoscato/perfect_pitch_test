from synthesizer import Player, Synthesizer, Waveform
import random
import round_up_methods as rup

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=0.8, use_osc2=False)

tuning = 440
semitone_increment = 1.05946
play_time = 1

lowest_freq = 16.35
highest_freq = 7902.13
notes = []
note_names = []

absolute_note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_ranges = [0, 1, 2, 3, 4, 5, 6, 7, 8]
C_freqs = [16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01]
non_C_freqs = []

for i in C_freqs:  # Iterate through C frequencies; seems harder than it should be, but it's the only way I can think of to keep true to the equal temperament note frequencies.
    for b in range(1, 12):  # Make 12 iterations to create a corresponding number of new frequencies
        new_freq = rup.round_half_down((i * (semitone_increment**b)), 2)
        non_C_freqs.append(new_freq)

all_freqs = sorted(C_freqs + non_C_freqs)

for i in note_ranges:  # Make complete list of note names
    for b in absolute_note_names:
        note_name = b + str(i)
        note_names.append(note_name)

note_dict_list = []
for i in range(len(all_freqs)):
    note_dict = {
        "name": note_names[i],
        "frequency": all_freqs[i],
    }
    note_dict_list.append(note_dict)

score = {
        "points": 0,
        "fails": 0,
    }

points = []
fails = []

duration = 10

for i in range(duration):
    new_note = note_dict_list[random.randint(20, len(note_dict_list)-10)]
    player.play_wave(synthesizer.generate_constant_wave(new_note['frequency'], play_time))
    answer = input('Which note was that:')
    if answer == new_note['name'][:-1]:
        print('Yes!')
        score['points'] += 1
    else:
        print('Nope, try again.')
        score['fails'] += 1

accuracy = score['points'] * 100 / (score['points'] + score['fails'])
print('Accuracy: ', str(accuracy), '%!')