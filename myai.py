import pyttsx3
import pywhatkit as kit
import datetime
import speech_recognition as sr
import os
import pyautogui
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again, please")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am salvin, please tell me how can I help you")
    
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "What do you get when you cross a snowman with a vampire? Frostbite!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "I used to play piano by ear, but now I use my hands.",
        "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
        "Why was the math book sad? Because it had too many problems.",
    ]
    joke = random.choice(jokes)
    speak(joke)

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "open cmd" in query:
            path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)
        elif "play video on youtube" in query:
            speak("Which video would you like me to play for you?")
            video_query = takecommand()
            kit.playonyt(video_query)
        elif "power off" in query:
            os.system("shutdown/s/t 1")
        elif "open powerpoint"in query:
            pyautogui.moveTo(740,1036,duration=1)
            pyautogui.click()
            pyautogui.write(' powerpoint',interval=0.25)
            pyautogui.press('enter')
        elif "write something" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
            speak("what should I write sir")
            typequery=takecommand()
            pyautogui.write(typequery)
        elif "excel"in query:
            pyautogui.moveTo(740,1036,duration=1)
            pyautogui.click()
            pyautogui.write(' excel',interval=0.25)
            pyautogui.press('enter')
        elif "do some calculation" in query:
            speak("Sure, what calculation would you like me to perform?")
            calc_query = takecommand()
            try:
                result = eval(calc_query)
                speak(f" is {result}")
            except Exception as e:
                speak("Sorry, I couldn't perform the calculation. Please try again.")
        elif "close youtube" in query:
            os.system("taskkill /im chrome.exe /f")
        elif "close notepad" in query:
            os.system("taskkill /im notepad.exe /f")
        elif "close powerpoint" in query:
            os.system("taskkill /im powerpnt.exe /f")
        elif "close cmd" in query:
            os.system("taskkill /im cmd.exe /f")
        elif "close excel" in query:
            os.system("taskkill /im excel.exe /f")
        elif "tell me a joke" in query:
            tell_joke()    
