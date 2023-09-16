import time
from random import random

import pyo

import amplitudes
import sharedvars
import asyncio

# Initialize the Pyo server
s = pyo.Server().boot()

# Set the sample rate (samples per second)
# s.setSr(44100)

# Define the base frequency and number of harmonics
base_freq = constants.base_frequency  # Hz
num_harmonics = constants.k

# Create amplitude values for each harmonic (change these as needed)

# Create a list of oscillators for the harmonics
oscillators = []

# Start the audio server
s.start()

# Initialize the mixer to dummy value
mixer = pyo.Mix(oscillators)
local_amplitudes = []
while True:
    await with sharedvars.lock:
        local_amplitudes = amplitudes.getAmplitudes()
    oscillators = [pyo.Sine(freq=base_freq * (i + 1), mul=amp) for i, amp in enumerate(local_amplitudes)]
    mixer = pyo.Mix(oscillators)
    mixer.out()
    time.sleep(.05)