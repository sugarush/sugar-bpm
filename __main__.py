from threading import Thread

import numpy as np
import sounddevice as sd
from aubio import dct
from glumpy import app

from visualizers.colors import Colors

window = app.Window()

active = 0
visualizers = [
    Colors()
]

@window.event
def on_draw(dt):
    window.clear()
    visualizers[active].quad.draw(visualizers[active].method)

@window.event
def on_key_press(symbol, modifiers):
    print(symbol, modifiers)

g = dct(16)

def bands(data):
    bands = g(data)
    return np.absolute(bands)

def audio_input_callback(indata, frames, time, status):
    data = indata.transpose()[0]
    visualizers[active].input(data, bands(data))

audio_input_stream = sd.InputStream(channels=1, callback=audio_input_callback, dtype='float32', latency='low')
audio_thread = Thread(target=audio_input_stream.start)
audio_thread.start()

app.run()
