import threading
import numpy
import pyo

init_lock = threading.Lock()
with init_lock:
    k = 7
    m = 1080
    n = 720
    base_frequency = 100
    buffer_ms = 100
    amplitudes_lock = threading.Lock()
    depthmap_lock = threading.Lock()
    volume_slider_lock = threading.Lock()
    kbyk_depthmap = numpy.zeros((m, n))
    volume_slider = 0
    amplitudes = [0 for i in range(k**2)]
    amplitudes_after_volume = amplitudes
    oscillators = []
    exiting = False