# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import multiprocessing
import threading

import amplitudes
import camera
#import graph
import gui
import synthesizer
import depthmap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    camera_thread = threading.Thread(target=camera.update_depth_map) # this should be refactored immediately
    depthmap_thread = threading.Thread(target=depthmap.update_amplitudes)
    #amplitudes_thread = threading.Thread(target=amplitudes.update_amplitudes)
    synth_thread = threading.Thread(target=synthesizer.play_synth)
    #graph_thread = threading.Thread(target=graph.animate_harmonics())
    # gui_thread = threading.Thread(target=gui.run_gui)
    camera_thread.start()
    depthmap_thread.start()
    #amplitudes_thread.start()
    synth_thread.start()
    #graph_thread.start()

    # gui_thread.start()
    gui.run_gui()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
