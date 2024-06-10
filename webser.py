import pyttsx3 as p
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

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

query = comd().lower()
engine = p.init() 
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googlescrap
        query = query.replace("sage","")
        query = query.replace("search","")
        query = query.replace("google","")
        speak("This is what I found: ")

        try:
            pywhatkit.search(query)
            result = googlescrap.summary(query,2)
            speak(result)

        except:
            speak("Could not find anything relevent")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found: ")
        query = query.replace("sage","")
        query = query.replace("search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "tell me about" in query:
        query = query.replace("sage","")
        query = query.replace("search","")
        query = query.replace("tell me about","")
        speak("This is what I found: ")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results)


