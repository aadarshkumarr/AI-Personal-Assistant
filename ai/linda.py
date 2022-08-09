import random
import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes
from gtts import gTTS
import playsound
from pyttsx3 import engine

engine = pyttsx3.init()

voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def hello(text):
    greet = ["hi", "hey", "hola", "wassup", "hello", "howdy", "what's good", "hey there"]
    response = ["hi", "hey", "hola", "wassup", "hello", "howdy", "what's good", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."
        return


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("hello you are up so late the")
    time()
    date()
    speak("linda at your service. Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(query)

    except Exception as e:

        speak("May I beg your pardon...")
        return "None"
    return query


def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)


def call(text):
    action_call = "Linda"
    text = text.lower()
    if action_call in text:
        return True
    return False


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abzc@gamil.com', '123')
    server.sendmail('abzc@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    global a
    a = a + 1
    hour = datetime.datetime.now().hour
    b = "ss" + str(time) + str(a) + ".png"

    img.save("C:\\Users\\adarsh.verma\\Desktop\\folder\\" + b)


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
while True:
    query = takeCommand().lower()
    print(query)
    if 'time' in query:
        time()
    elif 'date' in query:
        date()

    elif 'neha' in query:
        speak("yes one of my dumbest friend")

    elif "who are you" in query:
        speak("Hello I'm Linda your Personal AI Assistant")

    elif "tell me about yourself" in query:
        speak("Hello I'm Linda your Personal AI Assistant")

    elif "your name" in query:
        speak("My name is Linda")

    elif "who am i" in query:
        speak("you most probably be a human")

    elif "why do you exist" in query or "why did you come" in query:
        speak("It's a secret")

    elif "how are you" in query:
        speak("I'm fine thank you, what about you")

    elif "fine" in query or "good" in query:
        speak("good to hear that")

    elif "bad" in query or "not good" in query:
        speak("why what happen, is everything all right")

    elif "i love you" in query:
        speak("Thank you, i also love myself please keep loving me")

    elif "open" in query:
        if "browser" in query:
            speak("opening browser")
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        if "wps" in query:
            speak("opening WPS office")
            os.startfile(r"C:\Users\adarsh.verma\Desktop\WPS Office.lnk")

    elif 'tell me about' in query:
        speak("Searching...")
        query = query.replace("tell me about", "here what i got")
        result = wikipedia.summary(query, sentences=3)
        print(result)
        speak(result)
    elif 'who' in query:
        speak("Searching...")
        query = query.replace("who", "here what i got")
        result = wikipedia.summary(query, sentences=3)
        print(result)
        speak(result)
    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = 'aadarshkm01@gmail.com'
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Unable to send the email")

    elif 'search in chrome' in query:
        speak("What should i search ?")
        chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        search = takeCommand().lower()
        wb.get(chromepath).open_new_tab(search + '.com')

    elif 'logout' in query:
        os.system("shutdown -l")

    elif 'shutdown' in query:
        os.system("shutdown /s /t 1")

    elif 'restart' in query:
        os.system("shutdown /r /t 1")

    elif 'play songs' in query:
        songs_dir = 'D:\\Music'
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'remember that' in query:
        speak("What should I remember?")
        data = takeCommand()
        speak("you said me to remember that" + data)
        remember = open('data.txt', 'w')
        remember.write(data)
        remember.close()

    elif 'do you know anything' in query:
        remember = open('data.txt', 'r')
        speak("you said me to remember that" + remember.read())

    elif 'screenshot' in query:
        screenshot()
        speak("Done!")

    elif 'cpu' in query:
        cpu()

    elif 'joke' in query:
        jokes()

    elif 'offline' in query:
        quit()
