import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
 
def speak(audio): # programs jarvis to speak something  
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good evening!!")
    speak("Hello Sir, I am LUCY. Please tell me how may I help you")

def takeCommand(): #takes microphone input from the user and returns string output
    r = sr.Recognizer() #this class helps recognize audio
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5 #pause_threshold is seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 250 #energy_threshold is the minimum audio energy to consider for recording
        r.phrase_threshold = 0.5 #phrase_threshold is the minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email-id@gmail.com', 'your-password')
    server.sendmail('your-email-id@gmail.com, to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2) #takes two sentences from wikipedia
            print(results)
            speak("According to wikipedia")
            speak(results)
            
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'music' in query:
            music_dir = 'path_to_music_folder'
            songs = os.listdir(music_dir)
            print(songs)
            length = len(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}") 

        elif 'code' in query:
            codePath = "path_to_vscode_exe_file"         
            os.startfile(codePath)

        elif 'quit' in query:
            speak("Alright, sir. Bye Bye..")
            exit()

        elif 'email to anon' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'your-email-id@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email")
    
        

            

