import threading
import numpy

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
amplitudes = []
oscillators = []
exiting = False
