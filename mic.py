import sounddevice as sd
import tkinter as tk
from tkinter import ttk
import threading

duration = 10000  # seconds
volume_factor = 1  # Initial volume

# Function to update the volume_factor
def update_volume(value):
    global volume_factor
    volume_factor = float(value)
    if volume_factor == 0:
        volume_factor = 0.001  # Set a small non-zero value to prevent muting
    print(f"Volume Factor: {volume_factor:.2f}")

# Callback function for audio processing
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata * volume_factor

# Function to start the audio stream in a separate thread
def start_audio_stream():
    with sd.Stream(channels=2, callback=callback, blocksize=4096):
        sd.sleep(int(duration * 1000))

# Create the main application window
root = tk.Tk()
root.title("Volume Control")

# Create a label
label = ttk.Label(root, text="Volume Control")
label.pack()

# Create a slider
slider = ttk.Scale(root, from_=0.0, to=1.0, orient="horizontal", command=update_volume)
slider.set(volume_factor)
slider.pack()

# Create a thread to start the audio stream
audio_thread = threading.Thread(target=start_audio_stream)

# Function to stop the audio stream when the Tkinter window is closed
def on_closing():
    sd.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the audio stream in the separate thread
audio_thread.start()

# Run the Tkinter main loop
root.mainloop()
