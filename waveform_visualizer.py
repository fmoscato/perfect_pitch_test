import numpy as np
import matplotlib.pyplot as plt

amplitude = 1
frequency = 440
duration = 1
sampling_rate = 44100  # the number of samples per second

# create a time array
t = np.linspace(0, duration, int(sampling_rate * duration), False)

# generate the sine wave
waveform = amplitude * np.sin(2 * np.pi * frequency * t)

plt.plot(t, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()