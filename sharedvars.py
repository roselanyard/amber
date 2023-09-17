import threading
import numpy
import pyo

init_lock = threading.Lock()
with init_lock:
    k = 8
    base_frequency = 100
    buffer_ms = 100
    amplitudes_lock = threading.Lock()
    depthmap_lock = threading.Lock()
    volume_slider_lock = threading.Lock()
    kbyk_depthmap = numpy.zeros((k, k))
    volume_slider = 0
    amplitudes_L = [0 for i in range(int((k**2) / 2))]
    amplitudes_R = [0 for i in range(int((k ** 2) / 2))]
    amplitudes_after_volume_L = amplitudes_L
    amplitudes_after_volume_R = amplitudes_R
    oscillators_L = []
    oscillators_R = []
    volume = 0
    exiting = False