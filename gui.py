import asyncio
import tkinter as tk
from pyo import *

import sharedvars


# Function to update the label text with the slider value
def update_label_and_volume(val):
    label.config(text=f"Volume: {val}")
    # Update the amplitudes based on the slider value
    slider_value = float(val) / 100.0
    asyncio.run(update_volume(val))


async def update_volume(val):
    async with sharedvars.volume_slider_lock:
        for i, amp in enumerate(sharedvars.amplitudes):
            sharedvars.oscillators[i].mul = amp * val


# Create the main window
def run_gui():
    root = tk.Tk()
    root.title("Slider Example")

    # Create a label to display the slider value
    label = tk.Label(root, text="Volume: 0")
    label.pack()

    # Create a slider
    slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_label_and_volume)
    slider.pack()

    # Create a button to open the Pyo GUI
    # pyo_button = tk.Button(root, text="Open Pyo GUI", command=open_pyo_gui)
    # pyo_button.pack()

    # Run the Tkinter main loop
    root.mainloop()
