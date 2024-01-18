import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

print ("initializing black")

MASTER = "dimas"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[1].id)

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good afternoon love" + MASTER)
    else:
        speak("Good night love" + MASTER)
        speak("")

# microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        query = None

    return query

#main start here
speak("hallo dimas my name is latifa what can i help you ?")
wishMe()
query = takeCommand()

# logic for taks for query 
if "wikipedia" in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif "open youtube" in query.lower():
    url = "youtube.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "open google" in query.lower():
    url = "https://www.google.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "play music" in query.lower():
    songs_dir = "C:\\Users\\Dimas Maulana\\Music\\happy-asmara"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif "open whatsapp" in query.lower():
    url = "https://web.whatsapp.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "the time" in query.lower():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")  
    speak(f"{MASTER} the time is {strtime}")    

elif "local" in query.lower():
    url = "http://localhost/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "database" in query.lower():
    url = "http://localhost/phpmyadmin/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

# elif "books" in query.lower():
#     app_path = "C:/Program Files/Oracle/VirtualBox/VirtualBox.exe %s"
#     open(app_path)

# elif "sane" in query.lower():
#     app_path = "C:/xampp/xampp-control.exe %s"
#     webbrowser.get(app_path)