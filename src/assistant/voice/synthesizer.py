import pyttsx3
from config.settings import VOICE_ENGINE

engine = pyttsx3.init(VOICE_ENGINE)

def speak(text):
    engine.say(text)
    engine.runAndWait()
