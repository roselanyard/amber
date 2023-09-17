# This module will generate the amplitudes for each harmonic based on the depth of each "pixel" in the k*k array.
import sharedvars
import asyncio
from random import random
import time
local_kbyk_depthmap = [0 for n in range(sharedvars.k ** 2)]

def update_amplitudes():
    while not (sharedvars.exiting):
        with sharedvars.amplitudes_lock:
            global local_kbyk_depthmap
            local_kbyk_depthmap = sharedvars.kbyk_depthmap

        sharedvars.amplitudes_L = [0.5 - random()/8 for i in range(sharedvars.k**2)]  # placeholder values
        sharedvars.amplitudes_R = [0.5 - random()/8 for i in range(sharedvars.k**2)]  # placeholder values

        time.sleep(0.1)