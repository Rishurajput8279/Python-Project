import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import requests
import musicLibarby
import pygame
import os
from gtts import gTTS
from openai import OpenAI
newsapi="781e4c461580435ba0e96f7cfd9807a4"
#recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speech_old(text):
    engine.say(text)
    engine.runAndWait()
def speech(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize Pygame mixer
    pygame.mixer.init()
    
    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")
    
    # Play the MP3 file
    pygame.mixer.music.play()
    
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
        api_key="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",
        )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like in alexa and google cloud. Give short responses"},
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.in")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibarby.music[song]
        webbrowser.open(link)
    elif "news" in c:
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=781e4c461580435ba0e96f7cfd9807a4")
        if r.status_code == 200:
            data = r.json()
            # Extract all titles into a list
            if 'articles' in data:
                titles = [article['title'] for article in data['articles'] if 'title' in article]
                for i in titles:
                    speech(i)
            else:
                speech("No articles found in the response.")
    elif "search" in c:
        search_query = c.lower().replace("search", "").strip()  # Extract query
        search_url = f"https://www.google.com/search?q={search_query}"  
        webbrowser.open(search_url)
        speech(f"Searching Google for {search_query}")
    else:
        output=aiProcess(c)
        speech(output)

    
if __name__=="__main__":
    speech("initializing yours personal assistant....")
    #Listen for the wake word jarvis.....
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recorgnication")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=3)
            word=r.recognize_google(audio)
            if(word.lower() == "assistant"):
                speech("ya")
                with sr.Microphone() as source:
                    print("assistent Activate..")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
            # print(command)
            elif(word.lower()=="bye"):
                speech("have a nice day... bye")
                break
        except Exception as e:
            print("error {0}".format(e))
