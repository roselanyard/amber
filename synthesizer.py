import time
from random import random

import pyo

import amplitudes
import sharedvars
import asyncio

local_amplitudes = []


async def update_local_amplitudes():
    async with sharedvars.amplitudes_lock:
        global local_amplitudes
        local_amplitudes = await amplitudes.getAmplitudes()


def play_synth():
    s = pyo.Server().boot()

    # Set the sample rate (samples per second)
    # s.setSr(44100)

    # Define the base frequency and number of harmonics
    base_freq = sharedvars.base_frequency  # Hz
    num_harmonics = sharedvars.k

    # Create amplitude values for each harmonic (change these as needed)

    # Create a list of oscillators for the harmonics
    oscillators = []

    # Start the audio server
    s.start()

    # Initialize the mixer to dummy value
    mixer = pyo.Mix(oscillators)

    while True:
        asyncio.run(update_local_amplitudes())
        oscillators = [pyo.Sine(freq=base_freq * (i + 1), mul=amp) for i, amp in enumerate(local_amplitudes)]
        mixer = pyo.Mix(oscillators)
        mixer.out()
        time.sleep(.05)
