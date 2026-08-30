import whisper
model = whisper.load_model("medium")
import numpy as np
import pyperclip

def transcribe():
    audio = np.load("audio.npy")
    result = model.transcribe(audio, fp16=False)
    text = result["text"].strip()
    pyperclip.copy(text)
    print(text)
    print("---")
    print("Transcripción copiada al portapapeles.")

if __name__ == '__main__':
    transcribe()