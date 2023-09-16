import time
from random import random

import pyo
# import mic
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
        sharedvars.amplitudes_L = [0 for i in range(sharedvars.k**2)]
        sharedvars.amplitudes_R = [0 for i in range(sharedvars.k ** 2)]
        sharedvars.oscillators_L = [pyo.Sine(freq=i + 1, mul=0) for i in range(sharedvars.k ** 2)]
        sharedvars.oscillators_R = [pyo.Sine(freq=i + 1, mul=0) for i in range(sharedvars.k ** 2)]
        for i in range(sharedvars.k**2):
            sharedvars.oscillators_L[i] = pyo.Sine(freq = (i+1)*base_freq, mul = 0)
            sharedvars.oscillators_R[i] = pyo.Sine(freq=(i + 1) * base_freq, mul=0)
            sharedvars.oscillators_L[i].out()
            sharedvars.oscillators_R[i].out()
        while not sharedvars.exiting:
            for i in range(sharedvars.k**2):
                sharedvars.oscillators_L[i].stop()
                sharedvars.oscillators_R[i].stop()
                sharedvars.oscillators_L[i] = pyo.Sine(freq = (i+1)*base_freq, mul = sharedvars.amplitudes_L[i]*sharedvars.volume)
                sharedvars.oscillators_R[i] = pyo.Sine(freq = (i+1)*base_freq, mul = sharedvars.amplitudes_R[i]*sharedvars.volume)
                sharedvars.oscillators_L[i].out(chnl = 0)
                sharedvars.oscillators_R[i].out(chnl = 1)

            time.sleep(0.1)