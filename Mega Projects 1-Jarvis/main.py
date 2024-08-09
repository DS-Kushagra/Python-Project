import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR API"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize the mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def AIprocess(command):
    client = OpenAI(
  api_key="YOUR API")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in professional tasks like Alexa and Google Cloud. Give short responses."},
        {"role": "user", "content":command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r  = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = AIprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("At your service")
                #Listen fo command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))


