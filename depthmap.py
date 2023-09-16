import asyncio

import numpy

import sharedvars

local_depth_map = numpy.zeros((depthmap_m, depthmap_n))
def updateDepthMap():
    await with sharedvars.amplitudes_lock():
