# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import multiprocessing

import amplitudes
import gui
import synthesizer
import depthmap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    depthmap_proc = multiprocessing.Process(target=depthmap.updateDepthMap())
    amplitudes_proc = multiprocessing.Process(target=amplitudes.get_amplitudes())
    synth_proc = multiprocessing.Process(target=synthesizer.play_synth())
    gui_proc = multiprocessing.Process(target=gui.run_gui())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
