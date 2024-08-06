import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import numpy as np
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from googlesearch import search
import math
import requests
import time
from word2number import w2n
import flask
import pyscript
import pywhatkit

guifile='J.A.R.V.I.S_GUI.html'
os.system(f'start {guifile}')

'''complete this'''
def chat(query):pass

'''complete this'''
def send_email(query):pass

'''complete this'''
def send_message(query):pass

'''complete this'''
def read_notifications(query):pass

'''complete this'''
def make_call(query):pass

def play_song(query):
    # Let's create a list of terms to search for and an empty list for links
    song=query.partition('play')[2]
    pywhatkit.playonyt(song)
    say(f'playing {song} on you-tube')

'''complete this'''
def music_control(query):
    pass

'''complete this'''
def volume_control(query):
    pass

'''test this'''
def calc(query):
    query=query.partition('calculate')[2].split()
    functions=['add','plus','minus','subtract','multipy','into','devide','log','to the power','sin','cos','tan','factorial']
    if 'add' in query or 'plus' in query:
        num1=w2n.word_to_num(query[0])
        num2=w2n.word_to_num(query[2])
        say(f'answer is {num1+num2}')
    elif 'minus' in query or 'subtract' in query:
        num1=w2n.word_to_num(query[0])
        num2=w2n.word_to_num(query[2])
        say(f'answer is {num1-num2}')
    elif 'multiply' in query or 'into' in query :
        num1=w2n.word_to_num(query[0])
        num2=w2n.word_to_num(query[2])
        say(f'answer is {num1*num2}')
    elif 'devide' in query:
        num1=w2n.word_to_num(query[0])
        num2=w2n.word_to_num(query[2])
        if num2!=0:            
            say(f'answer is {round(num1/num2,2)}')
        else:
            say('cant devide by 0')
    elif 'log' in query:
        num1=w2n.word_to_num(query[1])
        say(f'answer is {math.log(num1)}')
    elif 'to the power' in query:
        num1=w2n.word_to_num(query[0])
        num2=w2n.word_to_num(query[4])
        say(f'answer is {num1**num2}')
    elif 'sine' in query:
        num1=w2n.word_to_num(query[1])
        say(f'answer is {math.sin(num1)}')
    elif 'cos' in query:
        num1=w2n.word_to_num(query[1])
        say(f'answer is {math.cos(num1)}')
    elif 'tan' in query:
        num1=w2n.word_to_num(query[1])
        say(f'answer is {math.tan(num1)}')
    elif 'factorial' in query:
        num1=w2n.word_to_num(query[1])
        say(f'answer is {math.factorial(num1)}')

def reminder(query):
    query=query.partition('reminder')[2]
    file=open('reminders.txt','a+')
    data=eval(file.read())
    data.append(query)
    say('ok sir added to reminders')

def read_reminders():
    file=open('reminders.txt','r')
    data=eval(file.read())
    for line in data:
        say(line)
        print(line)
    
'''complete this'''
def del_reminder(query):
    query=query.partition('reminder')[2].split()[0]
    num=w2n.word_to_num
    file=open('reminders.txt','a+')
    data=eval(file.read())
    data.pop(query-1)
    say('ok sir deleted the reminder')
    
'''coomplete this'''
def set_alarm(query):
    pass

def set_timer(query):
    query=query.partition('timer for')[2].split()
    num=w2n.word_to_num(query[0])
    if query[1] in ['min','minutes','minute','mins']:
        total_seconds=num*60
    elif query[1] in ['sec','secs','seconds']:
        total_seconds=num
    for remaining_seconds in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        
        if remaining_seconds == 10:
            print("Starting 10-second countdown!", end="\r")
            time.sleep(1)  # To allow the message to be displayed for a second
            for i in range(10, 0, -1):
                say(f"{i:2d}")
                time.sleep(1)
            break

    say("Time's up!")

def news(query):
    def fetch_news(api_key, query, language='en'):
        url = f'https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            return news_data['articles']
        else:
            print(f"Failed to fetch news: {response.status_code}")
            return []

    def display_news(articles):
        c=0
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article['title']}")
            say(f"{idx}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published At: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")
            c+=1
            if c==5:
                break

    API_KEY = '30025516f0dd488291267022129d90d0'  # Replace with your NewsAPI key
    news_articles = fetch_news(API_KEY, query)
    display_news(news_articles)

'''fix error'''
def get_weather(city='kuwait'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid=50430183ead39c8837b51304a7efeb79&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
        say(f"Temperature: {temperature}°C")
        say(f"Pressure: {pressure} hPa")
        say(f"Humidity: {humidity}%")
        say(f"Description: {weather_description}")
    else:
        print("City Not Found!")
        say("City Not Found!")

def say(text):
    engine= pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.say(text)
    print(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            return "Some Error Occurred."

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            query=query.lower()
            query = query.split()
            queries=[]
            sen=''
            c=0
            for word in query:    
                if word in ['open','play','search','tell','find','what',"what's",'start','set','calcuate']:
                    c+=1
                    if c>1:
                        queries.append(sen)
                        sen=''
                sen+=word+' '
            queries.append(sen)
            return queries
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

apps = [['whatsapp',"C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2424.6.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"],
        ['spotify', r'C:\Users\ragha\AppData\Local\Microsoft\WindowsApps\Spotify.exe'],
        ['armoury',"C:\\Users\\ragha\\AppData\\Local\\Microsoft\\WindowsApps\\ArmouryCrate.exe"],
        ['calculator',],
        ['blender',"C:\\Users\\ragha\\AppData\\Local\\Microsoft\\WindowsApps\\blender-launcher.exe"],
        ['vs code',"C:\\Users\\ragha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
        ['powerpoint',"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"],
        ['word',"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"],
        ['excel',"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"],
        ['davinchi',"C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Resolve.exe"],
        ['inkscape',"C:\\Program Files\\WindowsApps\\25415Inkscape.Inkscape_1.3.2.0_x64__9waqn51p1ttv2\\VFS\\ProgramFilesX64\\Inkscape\\bin\\inkscape.exe"],
        ['photoshop',r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe"],
        ['premire pro',r"C:\Program Files\Adobe\Adobe Premiere Pro 2024\Adobe Premiere Pro.exe"],
        ['illustrator',r"C:\Program Files\Adobe\Adobe Illustrator 2024\Support Files\Contents\Windows\Illustrator.exe"],
        ['black ops 3',r"C:\Users\ragha\OneDrive\Documents\cod bo3\boiii.exe"],
        ['war robots',"C:\\Program Files\\WindowsApps\\XDEVS.WWRWorldofWarfareRobotsOnline_3.25.10.0_x64__7yw2516a0mwqy\\WWR.exe"]
        ]
sites = [["youtube music","https://music.youtube.com/"],
        ["youtube", "https://www.youtube.com"], 
        ["desi cinema", "https://desicinemas.tv"],
        ["wikipedia", "https://www.wikipedia.com"], 
        ["google", "https://www.google.com"],
        ['redit',"https://www.reddit.com/?rdt=42748"],
        ['bear tracks','https://www.beartracks.ualberta.ca/psc/uahebprd/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL']
        ]

def Execution(command):
    try:
        site_found = 0
        for site in sites:
            if f"{site[0]}".lower() in command and ("open" in command or "start" in command):
                site_found = 1
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                break  # Break out of the loop since site is found

        if site_found == 0:  # Continue only if site was not found
            app_found = 0
            for app in apps:
                if f"{app[0]}".lower() in command and ("open" in command or "start" in command):
                    say(f"Opening {app[0]} sir...")
                    app_found = 1
                    subprocess.call(app[1])
                    break  # Break out of the loop since app is found

        if site_found == 0 and app_found == 0:  # Continue only if neither site nor app was found
            if "the time" in command:
                hour = datetime.datetime.now().strftime("%I")
                min = datetime.datetime.now().strftime("%M")
                am_pm = datetime.datetime.now().strftime('%p')
                say(f"Sir time is {hour}:{min} {am_pm}")

            elif "search" in command:
                webbrowser.open(command)

            elif 'tell' in command or "what's" in command or 'what' in command or 'find' in command:                            
                if 'news' in command:
                    news(command)
                elif "whether" in command:
                    get_weather()
                else:    
                    result = list(search(command, advanced=True, num_results=1))
                    say(result[0].description)

            elif "play" in command:
                play_song(command)

            elif any(word in command for word in ['resume','pause','stop','next','skip','loop']):pass
            elif any(word in command for word in ['increase','decrease','mute']):pass
            elif 'set' in command and "alarm" in command:pass
            elif 'set' in command and "timer" in command:
                set_timer(command)
            elif 'set' in command and "reminder" in command:
                reminder(command)
            elif 'read' in command and "reminders" in command:
                read_reminders()
            elif "screenshot" in command :
                pywhatkit.take_screenshot('screenshot')
            elif ('delete' in command or 'remove' in command) and "reminder" in command:pass

            elif "calculate" in command:pass
            else:
                pass
    except:
        say('sorry sir didnt understand that')
    
if __name__ == '__main__':
    while True:
        print('listening')
        perm=takeCommand().lower()
        print(f'user:{perm}')
        if "jarvis" in perm or "wake up" in perm:
            print('initialising jarvis')
            say("hello sir, how may I help you ")
            count=0
            while True:
                print('listenting...')
                rec=takeCommands()
                end=False
                for k in rec:
                    print(k)
                    Execution(k.lower())
                    if 'quit'in k or'shutdown'in k or'shut up'in k or'take rest' in k or "thank you" in k or "no jarvis" in k:
                        say('thank you sir, have a nice day')
                        end=True
                        break
                if end==True:
                    break
                else:
                    if count<3:
                        say('is there anything i can do sir ?')
                        count+=1
                    else:
                        break
                
