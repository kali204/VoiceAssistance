import sys
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

class VoiceAssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Assistant")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        self.label = QLabel("Click 'Speak' to give a command:")
        layout.addWidget(self.label)
        
        self.button = QPushButton("Speak")
        self.button.clicked.connect(self.process_command)
        layout.addWidget(self.button)
        
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        layout.addWidget(self.text_output)
        
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Request error: {e}")
            return ""

    def process_command(self):
        command = self.take_command()
        if command:
            self.text_output.clear()
            self.text_output.append(f"User Command: {command}")
            # Add logic to process the command here
            # For example, you could call your voice assistant functions based on the recognized command
            self.speak("Executing command")

def run_voice_assistant():
    app = QApplication(sys.argv)
    window = VoiceAssistantGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_voice_assistant()
