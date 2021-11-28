
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import pywhatkit as kit
import sys
import phonenumbers
import folium
import pyjokes
import opencage
import json
from txt import number
from phonenumbers import geocoder
import requests
import ctypes
import subprocess
from playsound import playsound
from plyer import notification
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omlandge0000@gmail.com', 'om@@11om')
    server.sendmail('landgepradnya1@gmail.com', to, content)
    server.close()

def make_request(url):
  response = requests.get(url)
  return response.text

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("sir, How are you?")
            hw = takeCommand().lower()
            if 'fine' in hw or 'good' in hw or 'nice' in hw or 'awesome' in hw:
               speak("It's good to know that your " + f"{hw}")
 
        
        # elif "change my name to" in query:
        #     query = query.replace("change my name to", "")
           
 
        # elif "change name" in query:
        #     speak("What would you like to call me, Sir ")
        #     assname = takeCommand()
        #     speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            assname = "assistant"
            speak("My friends call me")
            speak(f"{assname}")
            print("My friends call me", f"{assname}")
 
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'open my website' in query:
            webbrowser.open("http://choiceenterprises.atwebpages.com/")

        elif 'open google' in query:
            speak("Sir, what should I search...")
            gs = takeCommand().lower()
            kit.search(f"{gs}")
            print("Searching...")
        
        # elif 'search google' in query:
        #     speak("Sir, what should I search...")
        #     gsi = takeCommand().lower()
        #     kit.info(f"{gsi}", lines = 2)
        #     print("\nSuccessfully Searched")
        
        elif 'play youtube' in query:
            speak("Sir, what should I play...")
            yp = takeCommand().lower()
            kit.playonyt(f"{yp}")
            print("Playing...")

        # elif 'open payment slip' in query:
        #     webbrowser.open("http://choiceenterprises.atwebpages.com/admin/york_sep21/")   
        
        elif 'send message' in query:
            speak("Sir, what should you want to message...")
            wm = takeCommand().lower()
            minutes = int(datetime.datetime.now().minute)
            hours = int(datetime.datetime.now().hour)
            kit.sendwhatmsg("+918177875051",f"{wm}" ,hours, minutes+1 )


        elif 'play music' in query:
           music_dir = 'D:\\vids\\music'
           songs = os.listdir(music_dir)
           print(songs)    
           os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'my name' in query:   
            # speak("Om Bajirao")
            playsound('mp3/name.mp3')
        
        elif 'my mother name' in query:   
            # speak("Ujwala Bajirao")
            playsound('mp3/mummyname.mp3')
        
        elif 'my sister name' in query:   
            speak("Pradnya Bajirao")
            # playsound('mp3/pname.mp3')
        
        elif 'my father name' in query:   
            # speak("Bajirao Balasaheb")
            playsound('mp3/pappaname.mp3')
        
        elif 'my father work' in query:   
            speak("Business Man")

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('img/screenshot.png')
            speak('Screenshot taken.') 

        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)       
        
        elif 'covid stats' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            tc = print('total cases : ', total_cases)
            speak("Total Cases are :" + f"{total_cases}")
            nc = print('new cases', new_cases[1:])
            speak("New Cases are :" + f"{new_cases[1:]}")
            rc = print('total recovered', total_recovered)
            speak("Total recovered Cases are :" + f"{total_recovered}")
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
                title="COVID-19 Statistics",
                message=notification_message,
                timeout=5
            )
            speak("here are the stats for COVID-19")

        elif 'open map' in query: 
            speak("Sir, which location should I search...")
            gm = takeCommand().lower()
            if 'my home' in gm:
               webbrowser.open("https://earth.google.com/web/data=Mj8KPQo7CiExa0FZME1DSHB6bGFERmJXWUNkb0hmb1V3TF9yV011YmESFgoUMEIxQUFGODczMDFFMDFEN0RBMTc")
            else :    
               url = "https://earth.google.com/web/search/"
               web = (url + f"{gm}")
               webbrowser.open(f"{web}")
            
        
        elif 'mobile location' in query:   
            pepnumber = phonenumbers.parse(number, "CH")
            location = geocoder.description_for_number(pepnumber, "en")
            print(location)
            from phonenumbers import carrier
            results = phonenumbers.parse(number, "RO")
            print(carrier.name_for_number(results, "en"))

            from opencage.geocoder import OpenCageGeocode
            key = '94b473f7379143888da6ff8212aea56f'
            geocoder = OpenCageGeocode(key)
            query2 = str(location)
            result = geocoder.geocode(query2)

            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']

            myMap = folium.Map(location=[lat , lng], zoom_start=9)
            folium.Marker([lat,lng] , popup=location).add_to(myMap)

            strTime2 = datetime.datetime.now().strftime("%H_%M_%S")

            myMap.save("Location/"+ strTime2 +".html")
            mapOpen = "D:\\Python\\jarvis\\Location\\"+ strTime2 +".html"
            webbrowser.open(mapOpen)


       # elif 'open code' in query:
           # codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          #  os.startfile(codePath)

        elif 'email to pradnya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "landgepradnya1@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Om Sir. I am not able to send this email")   

        elif 'email to choice' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "choice.information@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Om Sir. I am not able to send this email")   

        elif 'email to om' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omlandge0000@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Om Sir. I am not able to send this email")   

        elif 'shutdown' in query:   
            speak("Thank Sir, have a good day...!")
            sys.exit()
        
        elif 'shut down' in query:   
            speak("Thank Sir, have a good day...!")
            sys.exit()