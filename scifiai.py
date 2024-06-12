import pyttsx3
import pywhatkit as kit
import datetime
import speech_recognition as sr
import os
import pyautogui
import random
import time
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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
            speak("")
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
    speak("I am Iris, please tell me how can I help you")  
    
def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "I used to play piano by ear, but now I use my hands.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "What do you call fake spaghetti? An impasta!",
        "What do you get if you cross a snowman and a vampire? Frostbite.",
        "Why did the math book look sad? Because it had too many problems.",
        "What’s orange and sounds like a parrot? A carrot.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "Why can't you give Elsa a balloon? Because she will let it go."
    ]
    joke = random.choice(jokes)
    speak(joke)

def pause_youtube_video():
    pyautogui.press('space')  

def skip_youtube_ad():
    ad_skipped = False
    attempts = 0
    while not ad_skipped and attempts < 5:  
        pyautogui.moveTo(1141, 706)
        pyautogui.click()
        time.sleep(0.5)
        ad_skipped = pyautogui.locateOnScreen('path_to_skip_ad_image.png', confidence=0.8) is None  # Check if skip button is gone
        attempts += 1
        time.sleep(1)

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
        elif "pause video" in query:
            pause_youtube_video()
        elif "skip ad" in query:
            skip_youtube_ad()
        elif "power off" in query:
            os.system("shutdown /s /t 1")
        elif "hi" in query:
            speak("hi")
        elif "what are you doing" in query:
            speak("nothing just listening")
        elif "you just rocking" in query:
            speak("thanks...")
        elif "you so cute" in query:
            speak("you to")
        elif "i am tired" in query:
            speak("take deep breath and just relax")
        elif "too slow" in query:
            speak("i am collecting information for you that's take time  ")
        elif "who is your favourite actor" in query:
            speak("absolutely that one and only thala ajith ")
        elif "what is your favourite sports" in query:
            speak("cricket ")
        elif "your favourite comics" in query:
            speak("marvel")
        elif "your favourite movie" in query:
            speak("titanic")
        elif "your favourite actress" in query:
            speak("sneha")
        elif "your favourite cricket team" in query:
            speak("csk")
        elif "your inspiration" in query:
            speak("my inspiration is Dr A.P.J.Abdul kalam sir ,because he show me the responsibility of every living beings and he is the greatest inspiration of all time")
        elif "are you hungry" in query:
            speak("no i am not hungry because i am an software based your personal assistant i want internet connection only")
        elif "you like csk" in query:
            speak("i like dhoni,so i like csk")
        elif "today work hard" in query:
            speak("just calm down,take deep breath ")
        elif "oh my god i am fearing" in query:
            speak(" all is well i am always with you")
        elif "who is my best friend" in query:
            speak("absolutely that's me")
        elif "open powerpoint" in query:
            pyautogui.moveTo(740, 1036, duration=1)
            pyautogui.click()
            pyautogui.write('powerpoint', interval=0.25)
            pyautogui.press('enter')
        elif "write something" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
            speak("What should I write, sir?")
            typequery = takecommand()
            pyautogui.write(typequery)
        elif "open excel" in query:
            pyautogui.moveTo(740, 1036, duration=1)
            pyautogui.click()
            pyautogui.write('excel', interval=0.25)
            pyautogui.press('enter')
        elif "open visual studio" in query:
            pyautogui.moveTo(740, 1036, duration=1)
            pyautogui.click()
            pyautogui.write('visual studio code', interval=0.25)
            pyautogui.press('enter')
        elif "do some calculation" in query:
            speak("Sure, what calculation would you like me to perform?")
            calc_query = takecommand()
            try:
                result = eval(calc_query)
                speak(f"The result is {result}")
            except Exception as e:
                speak("Sorry, I couldn't perform the calculation. Please try again.")
        elif "play music" in query:
            dir="c:\\Users\\KAVIN\Music\\music"
            songs=os.listdir(dir)
            rd=random.choice(songs)
            if rd.endswith('.mp3'):
                os.startfile(os.path.join(dir,rd))
        elif "close youtube" in query:
            os.system("taskkill /im chrome.exe /f")
        elif "close excel" in query:
            os.system("taskkill /im excel.exe /f")
        elif "close notepad" in query:
            os.system("taskkill /im notepad.exe /f")
        elif "close powerpoint" in query:
            os.system("taskkill /im powerpnt.exe /f")
        elif "close cmd" in query:
            os.system("taskkill /im cmd.exe /f")
        elif "close chrome" in query:
            os.system("taskkill /im chrome.exe /f")
        elif "tell me a joke" in query:
            tell_joke()
        elif "discover" in query:
            speak("What would you like me to discover?")
            discover_query = takecommand()
            speak("Searching on Wikipedia")
            results = wikipedia.summary(discover_query, sentences=2)
            speak(f"According to Wikipedia: {results}")
            print(results)
        elif "search for me" in query:
            speak("What would you like me to search for?")
            search_query = takecommand()
            kit.search(search_query)
        elif "short it" in query:
            speak("Which application would you like to minimize?")
            app = takecommand()
            if "chrome" in app:
                os.system("start /min chrome")
            elif "notepad" in app:
                os.system("start /min notepad")
            elif "powerpoint" in app:
                os.system("start /min powerpnt")
            elif "cmd" in app:
                os.system("start /min cmd")
            else:
                speak("Sorry, I couldn't find the specified application to minimize.")
