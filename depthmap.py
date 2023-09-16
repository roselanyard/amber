import asyncio

import numpy
import asyncio
import sharedvars
import camera

local_image = numpy.zeros((depthmap_m, depthmap_n))
async def updateDepthMap():
    async with sharedvars.amplitudes_lock():
        local_image = camera.get_greyscale_frame()
