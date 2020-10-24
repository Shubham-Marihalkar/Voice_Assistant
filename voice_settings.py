import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime


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


