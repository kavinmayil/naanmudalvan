import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

r = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        o = r.listen(source)
    try:
        print("Wait for a few moments")
        query = r.recognize_google(o, language="en-in")
        print("user said ", query)
    except Exception as e:
        print(e)
        speak("Say that Again Please ")
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boss")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")

if __name__ == "__main__":
    wishme()
    
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("Opening Boss")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Boss")
            webbrowser.open("google.com")

        elif "open code" in query:
            speak("Opening Boss")
            codepath = "C:\\Users\\Murali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open chrome" in query:
            speak("Opening Boss")
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
