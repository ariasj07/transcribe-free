import argparse
import whisper
import pyperclip

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe un archivo de audio/video usando Whisper."
    )

    parser.add_argument(
        "file",
        help="Ruta al archivo de audio o video (mp4, wav, ogg, mp3, etc.)"
    )
    parser.add_argument(
        "--language", "-l",
        default=None,
        help="Código de idioma (ej: es, en, pt). Si se omite, se autodetecta."
    )

    args = parser.parse_args()

    model = whisper.load_model("medium")
    print(f"Working with file: {args.file}...")
    print("Transcribing...")
    resultado = model.transcribe(args.file, language=args.language)
    pyperclip.copy(resultado)

    print(resultado["text"])
    print("---")
    print("Transcripción copiada al portapapeles.")

if __name__ == "__main__":
    main()