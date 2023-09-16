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
        for i, amp in enumerate(sharedvars.amplitudes):
            sharedvars.amplitudes_after_volume[i] = sharedvars.amplitudes[i] * val


# Create the main window
def run_gui():

    root.title("Slider Example")

    # Create a label to display the slider value

    label.pack()

    # Create a slider
    slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_label_and_volume)
    slider.pack()

    # Create a button to open the Pyo GUI
    # pyo_button = tk.Button(root, text="Open Pyo GUI", command=open_pyo_gui)
    # pyo_button.pack()

    # Run the Tkinter main loop

    root.mainloop()
    sharedvars.exiting = True