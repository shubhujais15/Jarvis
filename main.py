import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import musicLibrary
import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def ai_Process(command):
    # load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f""" 
You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and google cloud, don't ask question to me just give answer of what i ask. 
{command}
"""
    response = model.generate_content(prompt)
    return response.text


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
    elif "news" in c.lower():  # Check if the string 'news' is in the input 'c'
        try:
            news_api = os.getenv("NEWS_API_KEY")
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                
                if articles:  # Ensure there are articles in the response
                    for article in articles:
                        speak(article['title'])  # Assuming 'speak' is a text-to-speech function
                else:
                    speak("Sorry, no news articles available at the moment.")
            else:
                speak(f"Failed to retrieve news. Status code: {r.status_code}")
        except requests.exceptions.RequestException as e:
            speak(f"An error occurred while fetching news: {str(e)}")

    else:
        output = ai_Process(c)
        speak(output)



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