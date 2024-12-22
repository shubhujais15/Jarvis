import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open LinkedIn"  in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube"  in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


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
            word=r.recognize_google(audio)
            # Speak command
            if(word.lower()== "jarvis"):
                speak("Ya")

            #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error:{0}".format(e))