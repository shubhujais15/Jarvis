import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis")

    #Listen for wake word Jarvis
    #obtain audio from microphone
    while True:
        r = sr.Recognizer()
        

        # recognize speech using google
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=4,phrase_time_limit=1)
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Error:{0}".format(e))