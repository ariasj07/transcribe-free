import sounddevice as sd
import numpy as np
import keyboard
import sys
import os


def callback(indata, frames, time, status):
    grabacion.append(indata.copy())

def save_recording(audio):
    np.save("audio.npy", audio)

grabando = False
def al_presionar():
    global grabando, stream, grabacion
    if not grabando:
        grabando = True
        grabacion = []
        print("Grabando...")
        stream = sd.InputStream(samplerate=16000, channels=1, callback=callback)
        stream.start()

def al_soltar():
    global grabando, stream
    grabando = False
    print("Grabación finalizada")
    stream.stop()
    audio = np.concatenate(grabacion).flatten()
    save_recording(audio)
    os._exit(0)

if __name__ == '__main__':
    keyboard.on_press_key("f9", lambda _: al_presionar())
    keyboard.on_release_key("f9", lambda _: al_soltar())
    keyboard.wait()