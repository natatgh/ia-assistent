from src.assistant.voice.recognizer import recognize_speech
from src.assistant.voice.synthesizer import speak
from src.assistant.nlp.processor import process_command

def main():
    while True:
        command = recognize_speech()
        if command:
            response = process_command(command)
            speak(response)

if __name__ == "__main__":
    main()
