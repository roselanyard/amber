import asyncio
k = 7
m = 1080
n = 720
base_frequency = 100
buffer_ms = 100
amplitudes_lock = asyncio.Lock()
depthmap_lock = asyncio.Lock()
kbyk_depthmap = numpy.zeros((depthmap_m, depthmap_n))