import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time
from googlesearch import search
import subprocess#to open a file location in explorer
import random
  
# for youtube search
import urllib.request
import urllib.parse
import re

#for weathe reports
import requests
from pprint import pprint


engine = pyttsx3.init('sapi5')#main engine to respond in voice 
''' voice setting function '''
def voicegenerator():
    global engine 
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)

''' speak function '''
def speak(audio):
    global engine
    engine.say(audio)
    engine.runAndWait()


''' greeting function for starting convo '''
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    
    speak(" hello sir,Asus here!,Please tell me how may I help you")       


''' function to taje voice commands '''
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def process_command(query):
    if True:
            #hot word detection
            query = query.replace("mari", "")
            query = query.replace("maari", "")
            query = query.replace("hey", "")
          # Logic for executing tasks based on query
            if 'time now' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<5:
                    speak(f"Sir, the time is {strTime}")
                    speak("Sir its been long time you are working ,please have some rest")
                elif hour>=5 and hour<12:
                    speak("Good Morning!")   
                elif hour>=12 and hour<18:
                    speak("Good Afternoon!")   
                else:
                    speak("Good Evening!")  
            
            elif 'date today' in query or "today's date" in query:
                print(ctime())
                speak(ctime())

            elif 'hello there' in query:
                speak("Hello sir")

            elif "are you there" in query:
                speak("yes sir,Please tell me how may I help you")
    
            elif 'bye' in query:
                speak("Bye for now sir,hope we will meet very soon")
                return

            elif'tell me' in query or 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("tell me", "")
                query = query.replace("about", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    webbrowser.open("https://google.com/search?q=%s" % query)
                    speak('Sir,the search result are')

            elif 'thanks' in query or 'thank you' in query:
                speak('you are welcome sir')
            else:
                print("\n")
                return


######################################   M A I N   F U N C T I O M   ##################################

if __name__ == "__main__":
    voicegenerator()
    #greet()

    while True:
        query = takecommand().lower()
        if "hey" in query or "hay" in query or "hai" in query:
            speak('Hmmmmm')
            time.sleep(0.05)
            query = takecommand().lower()
            process_command(query)
        
            
                
            
       
        

        
