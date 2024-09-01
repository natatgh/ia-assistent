import speech_recognition as sr
from config.settings import LANGUAGE

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language=LANGUAGE)
            print(f"Você disse: {command}")
            return command
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
            return ""
        except sr.RequestError:
            print("Erro ao conectar ao serviço de reconhecimento de fala.")
            return ""
