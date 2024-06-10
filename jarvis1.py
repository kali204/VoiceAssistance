import time
import os
import subprocess
import pyttsx3
import pyautogui
import requests
import speech_recognition as sr
from PIL import ImageGrab
from make_call import make_call
from threading import Thread



# Initialize the AI assistant
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12:
        speak("Good morning! I am your AI assistant, Jarvis. How can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon! I am your AI assistant, Jarvis. How can I help you?")
    else:
        speak("Good evening! I am your AI assistant, Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def write_to_notepad(content):
    pyautogui.hotkey('ctrl', 'a')  # Select all content
    pyautogui.press('delete')  # Delete the selected content
    pyautogui.write(content)  # Write content to Notepad

def open_notepad():
    subprocess.Popen(['notepad.exe'])
    speak("Sir what should i notedown")
    time.sleep(1)
    content = take_command()
    if content:
        write_to_notepad(content)

def take_screenshot():
    try:
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Get current timestamp
        file_name = f"screenshot_{timestamp}.png"   # Create filename with timestamp
        screenshot = ImageGrab.grab()  # Capture the entire screen
        screenshot.save(file_name)
        print(f"Screenshot saved as '{file_name}'")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

def get_location():
    try:
        ip_request = requests.get('https://api.ipify.org?format=json', timeout=5)
        if ip_request.status_code == 200:
            ip_address = ip_request.json()['ip']
            return ip_address
        else:
            return None
    except requests.RequestException as e:
        print(f"Failed to get IP address: {e}")
        return None


def get_weather():
    location = get_location()
    city="Bhimtal"
    api_key = '6c00b6539d656cff254ebd0da57c2da7'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            weather_info = (
                f"Weather in {city}:\n"
                f"Description: {weather_description}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            return weather_info
        else:
            return "Failed to retrieve weather information."
    except requests.RequestException as e:
        return f"Request error: {e}"
    except KeyError as e:
        return f"Data error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"


def handle_voice_command(command):
    if command.startswith("call"):
        parts=command.split("call")
        contact_name=parts[1].strip() if len(parts)>1 else None
        if contact_name:
                make_call(contact_name)
        else:
                speak("Please specify a contact to call.")
    else:
        print("Command not recognized.")

def main():
    greet()
    weather_data=get_weather()
    speak(weather_data)
    while True:
        query = take_command().lower()

        if query == 'quit':
            break

        if 'open notepad' in query:
            open_notepad()

        elif 'open chrome' in query:
            os.system('start chrome.exe')

        elif 'open google' in query:
            os.system('start https://www.google.com')

        elif 'play music' in query:
            os.system('start C:\\Users\\Username\\Music')

        elif 'the time' in query:
            strTime = time.strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'make a call' in query:
            speak("Sir to whome")
            user_command= take_command().lower()
            handle_voice_command(user_command)

        elif 'take a screenshoot' in query:
            take_screenshot()


        elif 'news' in query:
            from news import get_top_headlines
            news=get_top_headlines()
            for article in news:
                speak(article['title'])
                speak(article['summary'])

        elif 'exit' in query:
            speak("Thank you for using Jarvis! Have a great day!")
            exit()

           

if __name__ == '__main__':
    main()