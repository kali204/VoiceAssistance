import pyttsx3 as p
import speech_recognition 
import datetime
import pyautogui
import os

from Greet import greet
engine = p.init() 
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.say("Welcome , I'm sage")
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

if __name__ == "__main__":
    while True:
        query = comd().lower()
        if"wake up" in query:
            greet()
                   
            while True:
              query = comd().lower()
              if"wait" in query:
                    speak("I'm waiting,You can wake me anytime sir")
                    break
              elif"go to sleep" in query:
                  speak("Going to sleep")
                  exit()  

              elif"hello" in query:
                    speak("Hello Sir, How are you")
              elif"I am fine and you" in query or "I am good and you" in query or "I am great and you" in query:
                    speak("Great")
              elif"breakup" in query:
                  speak("I am not breaking up with you ,Sir")
              elif"what are you doing" in query:
                  speak("I am assisting you , Sir")              

              elif"open" in query:
                    from Dict import openapp
                    openapp(query)
              elif"close" in query:
                  from Dict import closeapp
                  closeapp(query)     
                       
              elif"google" in query:
                  from webser import searchGoogle
                  searchGoogle(query)  
              elif"youtube" in query:
                  from webser import searchYoutube
                  searchYoutube(query)
              elif"tell me about" in query:
                  from webser import searchWikipedia
                  searchWikipedia(query)

#controls for youtube only
              elif"pause" in query or "play" in query:
                  pyautogui.press("k")
              elif"mute" in query:
                  pyautogui.press("m")
                 
                     
              elif"the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(strTime) 
                    speak(f"Sir, The time is {strTime}")

              elif"whatsapp" in query:
                    from Whatsapp import sendMsg
                    sendMsg()
                     

              elif"shutdown the system" in query:
                  speak("Shutting down your system")      
                  os.system("shutdown /s /t 1")
              elif"restart the system" in query:
                  speak("restarting your system")      
                  os.system("shutdown -r -t 0")          
                                        