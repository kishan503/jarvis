import requests, geocoder
import pytz
import pyttsx3
import datetime
import requests
import bs4
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import operator

from wikipedia.wikipedia import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning Sir!")
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!")

    else:
        print("Good Evening Sir!")
        speak("Good Evening Sir!")

    print("I am JARVIS, Please tell me How may I help you?.")
    speak("I am JARVIS, Please tell me How may I help you?.")
    
def takeCommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Litsening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        return "None"

    return query

def taskexicution():
    wishme()
    while True:

        query=takeCommand().lower()
        
        if "what is" in query or "who is" in query:
            speak("Searching in Wikipedia....please wait")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia...")
            speak(results)

        elif "open google" in query:
            speak("opening google for you sir.")
            webbrowser.open("google.com")

        elif "open gmail" in query:
            speak("opening gmail for you sir.")
            webbrowser.open("gmail.com")

        elif "open youtube" in query:
            speak("opening youtube for you sir.")
            webbrowser.open("youtube.com")
            
        elif "what time is it" in query:
            strTime = datetime.datetime.now().strftime(r"%H:%M:%S")   
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Locating")
            speak(location)
            webbrowser.open(f"https://www.google.com/maps/place/"+location+"")
            
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = r"C:\\Users\\KISHAN\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ip = requests.get('http://api.ipify.org/').text
                location = geocoder.ip(ip)
                print(location.city,location.state, pytz.country_names[location.country])
                speak(f"Sir, I am not sure but we are in {location.city} city, which is situatate in {location.state} in {pytz.country_names[location.country]}")
                
            except Exception as e:
                speak("Sorry sir, i can not find our location due to internet issue")
                pass

        elif "write a note" in query:
            speak("What should i write sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'sure' in snfm:
                strTime = datetime.datetime.now().strftime(r"%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("Done sir")
            else:
                file.write(note)
                speak("Done sir")

        elif "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Sure what do you want to calculate sir?")
                print("Sure what do you want to calculate sir?")
                print("Litsening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:    
                print("Recognizing")
                query = r.recognize_google(audio, language='en-in')
                print(query)
            except Exception as e:
                print("Please say properly")
                speak("Please say properly")

            def get_operator(op):
                return{
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiplied by
                    'divided' : operator.truediv, #divided
                }[op]
            def exprations(op1,oper,op2):
                op1,op2 = int(op1),int(op2)
                return get_operator(oper)(op1,op2)
            speak("Your result is")
            print("Your result is")
            print(exprations(*(query.split())))
            speak(exprations(*(query.split())))
        
        elif "temperature" in query:
            speak("wait sir let me check")
            search = "temperature in Ahmedabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = bs4.BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")


        elif "who made you" in query:
            print("I am in this computer RIGHT?, So obveosly a HUMAN made me")
            speak("I am in this computer RIGHT?, So obveosly a HUMAN made me")

        elif "who are you" in query:
            print("I am JARVIS, A virtual artificial intelligence, And i am here to assist you veraity of task as best i can, 24 hours a day, 7 days a week.")
            speak("I am JARVIS, A virtual artificial intelligence, And i am here to assist you veraity of task as best i can, 24 hours a day, 7 days a week.")

        elif "who i am" in query:
            print("You are speaking, So definatly you are a HUMAN")
            speak("You are speaking, So definatly you are a HUMAN")

        elif "your creator name" in query:
            print("oh no i already told you one HUMAN made me for a reason,        And that HUMAN's name is KISHAN PANCHAL")
            speak("OH NO I already told you one HUMAN made me for a reason,        And that HUMAN's name is KISHAN PANCHAL")

        elif "how are you" in query:
            print("I am fine sir, what about you?")
            speak("I am fine sir, what about you?")

        elif "i am good" in query:
            print("Glad to here that sir")
            speak("Glad to here that sir")

        elif "what can you do" in query:
            print("I can do all the tasks which are in my task list, what can i do for you sir?")
            speak("I can do all the tasks which are in my task list, what can i do for you sir?")

        elif "stop" in query:
            print("Ok sir, but you can call me anytime.")
            speak("Ok sir, but you can call me anytime.")
            break
