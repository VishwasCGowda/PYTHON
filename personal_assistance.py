import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import pyjokes
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Please Enter your name")
    nam=input("Enter your name ")   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!" +nam)
    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+nam)   
    else:
        speak(" Good Evening!" + nam)  
    speak("I am your friend VISHWAS. An AI system, Please tell me how may I help you")       
    print("Try saying something")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing please wait for the result")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vishu@varzsecurity.com', 'your-password')
    server.sendmail('sanjay@gamil.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stavkoverflow")
            webbrowser.open("stackoverflow.com")   
        
        elif 'play music' in query:
            speak("Please enter the path that contains music you can copy and paste that")
            mpth = input("Please enter the path that contains music")
            music_dir = mpth
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Please enter the path which contains your code that to be show.")
            cpth=input("Please enter the code path, You can copy and paste that.")
            speak("code path you ented is" + cpth + "I thick that is correct" +nam)
            codePath = cpth
            os.startfile(codePath)
        
        elif 'browser' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening browser for you" +nam)

        elif 'who are you' in query:
            speak("I am your friend VISHWAS an AI system")

        elif 'joke' in query:
            speak("Getting you the joke please wait" +nam)
            speak(pyjokes.get_joke())
        
        elif 'quit' in query:
            speak("Have a good day Thank you for Using" +nam)
            speak("please press on the cross icon on the top right of the window or press alt+f4 button")

        elif 'exit' in query:
            speak("Have a good day Thank you for Using" +nam)
            speak("please press on the cross icon on the top right of the window or press alt+f4 button")

        elif 'email to VISHWAS' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vishwas@varzsecurity.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend vishwas. I am not able to send this email")   