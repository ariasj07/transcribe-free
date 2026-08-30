import whisper
model = whisper.load_model("medium")
import numpy as np

def transcribe():
    audio = np.load("audio.npy")
    result = model.transcribe(audio, fp16=False)
    print(result["text"].strip())
    return result["text"].strip()

if __name__ == '__main__':
    transcribe()