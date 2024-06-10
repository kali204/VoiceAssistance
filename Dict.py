import os
import pyautogui
import webbrowser
import pyttsx3 as p
from time import sleep
from AppOpener import open
from AppOpener import close

engine = p.init() 
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openapp(query):
    speak("Opening,Sir")
    if ".com" in query or ".org" in query or ".co.in" in query:
        query = query.replace("open","")
        query = query.replace("Sage","")
        query = query.replace("","")
        webbrowser.open(f"https://www.{query}")

    else:
        query = query.replace("open","")
        query = query.replace("Sage","")
        open(query)

def closeapp(query):
    speak("Closing,Sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Tab closed")
    else:
        query = query.replace("open","")
        query = query.replace("Sage","")
        close(query)

