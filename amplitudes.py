# This module will generate the amplitudes for each harmonic based on the depth of each "pixel" in the k*k array.
import sharedvars

local_kbyk_depthmap = [0 for n in range(sharedvars.k**2)]
def getAmplitudes():

    async with sharedvars.lock:
        local_kbyk_depthmap = sharedvars.kbyk_depthmap

    return [1.0, 0.5 - random(), 0.3, 0.6, 1.0 - random(),
     0.5, 0.2 - random(), 0.2, 0.2, 0.2 - random(), 0.2,
     0.2, 0.2, 0.2 - random(), 0.2, 0.2 - random(), 0.2 - random()] # placeholder values