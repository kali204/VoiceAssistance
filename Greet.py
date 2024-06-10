import pyttsx3 as p
import datetime

engine = p.init() 

engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 & hour<=12:
        speak("I'm up ,Sir")
    elif hour>=12 & hour<=18:
        speak("I'm up ,Sir") 
    else: 
        speak("I'm up ,Sir")

    speak("How can I help you?")  