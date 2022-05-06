import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit

# to generate random no. for song play
n = random.randint(0,9)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening!")

    speak("I am your assistant. Please tell how may I help you")

def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please pardon...")
        speak("Please pardon...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("xyz@gmail.com", 'XXXXX')
    server.sendmail('xyz@gmail.com', to,content)
    sever.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        #logic for executing tasks based on query
        if 'wikipedia' in query:
           speak('Searching wikipedia.......')
           query = query.replace("wikipedia", "")

           # it will return 2 sentences from wikipedia
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
    
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\OneDrive\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H;%M;%S")
            speak(f"Maam, The time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif "mail" in query:
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = "qwer@gmail.com"
                sendEmail(to, content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("Sorry Maam! I am unable to send your message at this moment!")
        
        elif "message" in query:
            pywhatkit.sendwhatmsg("+91........","This is an automate whatsapp message.",9,27)
        
