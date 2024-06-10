import pyttsx3 as p
import speech_recognition
import pywhatkit
#from bs4 import BeautifulSoup
import datetime
import webbrowser
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = p.init() 
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.runAndWait()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def comd():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print(f"Say that again")
        return "None"
    return query 

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMsg():
    speak("Whom do you want to text enter number")
    num = int(input("Whom do you want to text enter his or her number: "))
    text = str(input("Enter text: "))

    pywhatkit.sendwhatmsg(f"+91{num}",text,time_hour=strTime,time_min=update)

