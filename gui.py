import asyncio
import tkinter as tk
from pyo import *

import sharedvars
root = tk.Tk()
label = tk.Label(root, text="Volume: 0")

# Function to update the label text with the slider value
def update_label_and_volume(val):
    global label
    label.config(text=f"Volume: {val}")
    # Update the amplitudes based on the slider value
    slider_value = float(val) / 100.0
    update_volume(val)


def update_volume(val):
    with sharedvars.volume_slider_lock:
        #for i, amp in enumerate(sharedvars.amplitudes_L):
        #    sharedvars.amplitudes_after_volume_L[i] = sharedvars.amplitudes_L[i] * float(val)
        #    sharedvars.amplitudes_after_volume_R[i] = sharedvars.amplitudes_R[i] * float(val)
        sharedvars.volume = float(val)/100

# Create the main window
def run_gui():

    root.title("Amber")

    # Create a label to display the slider value

    label.pack()

    # Create a slider
    slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_label_and_volume)
    slider.pack()


    slider = tk.Scale(root, from_=0, to=sharedvars.k**2, orient="horizontal")
    slider.pack()

    # Create a button to open the Pyo GUI

    pyo_button = tk.Button(root, text="Toggle Harmonic Selection Mode")
    pyo_button.pack()

    # Run the Tkinter main loop

    root.mainloop()
    sharedvars.exiting = True