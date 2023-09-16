import time
from random import random

import pyo

import amplitudes
import sharedvars
import asyncio

def play_synth():
    s = pyo.Server().boot()

    # Set the sample rate (samples per second)
    # s.setSr(44100)

    # Define the base frequency and number of harmonics
    base_freq = sharedvars.base_frequency  # Hz
    num_harmonics = sharedvars.k

    # Create amplitude values for each harmonic (change these as needed)

    # Create a list of oscillators for the harmonics
    # sharedvars.oscillators = []
    # (already initialized)

    # Start the audio server
    s.start()
    with sharedvars.init_lock:
        sharedvars.amplitudes = [0 for i in range(sharedvars.k**2)]
        sharedvars.oscillators = [pyo.Sine(freq=i + 1, mul=0) for i in range(sharedvars.k ** 2)]
        for i in range(sharedvars.k**2):
            sharedvars.oscillators[i] = pyo.Sine(freq = (i+1)*base_freq, mul = 0)
            sharedvars.oscillators[i].out()
        while not sharedvars.exiting:
            for i in range(sharedvars.k**2):
                sharedvars.oscillators[i].stop()
                sharedvars.oscillators[i] = pyo.Sine(freq = (i+1)*base_freq, mul = sharedvars.amplitudes[i])
                sharedvars.oscillators[i].out()
            time.sleep(0.1)
