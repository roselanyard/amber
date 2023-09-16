import pyo

# Initialize the Pyo server
s = pyo.Server().boot()

# Set the sample rate (samples per second)
s.setSr(44100)

# Define the base frequency and number of harmonics
base_freq = 440  # Hz
num_harmonics = 5

# Create amplitude values for each harmonic (change these as needed)
amplitudes = [1.0, 0.5, 0.3, 0.2, 0.1]

# Create a list of oscillators for the harmonics
oscillators = [Sine(freq=base_freq * (i + 1), mul=amp) for i, amp in enumerate(amplitudes)]

# Mix the oscillators together
mixer = Mix(oscillators)

# Start the audio server
s.start()

# Start the mixer
mixer.out()

# Run for a specified duration (in seconds)
s.gui(locals())