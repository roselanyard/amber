import tkinter as tk
from pyo import *

# Initialize the Pyo server
s = Server().boot()
s.setSr(44100)

# Define the base frequency and number of harmonics
base_freq = 440  # Hz
num_harmonics = 5

# Create amplitude values for each harmonic (change these as needed)
amplitudes = [1.0, 0.5, 0.3, 0.2, 0.1]

# Create a list of oscillators for the harmonics
oscillators = [Sine(freq=base_freq * (i + 1), mul=0.0) for i in range(num_harmonics)]

# Mix the oscillators together
mixer = Mix(oscillators)

# Function to update the label text with the slider value
def update_label(val):
    label.config(text=f"Slider Value: {val}")
    # Update the amplitudes based on the slider value
    slider_value = float(val) / 100.0
    for i, amp in enumerate(amplitudes):
        oscillators[i].mul = amp * slider_value

# Function to open the Pyo GUI
def open_pyo_gui():
    s.gui(locals())

# Create the main window
root = tk.Tk()
root.title("Slider Example")

# Create a label to display the slider value
label = tk.Label(root, text="Slider Value: 0")
label.pack()

# Create a slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_label)
slider.pack()

# Create a button to open the Pyo GUI
pyo_button = tk.Button(root, text="Open Pyo GUI", command=open_pyo_gui)
pyo_button.pack()

# Run the Tkinter main loop
root.mainloop()