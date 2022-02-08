import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
        engine.say(audio)
        engine.runAndWait()


def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak("Good Morning!")
        elif hour>=12 and hour<18:
                speak("Good Evening!")
        else:
                speak("Good Evening!")
        speak("Hello dear.  My intro I am  Terrace  and i created by  Bharat  . I got invented at Hudson Lane . How can i serve you! ")

def takeCommand():

        r=sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening..!!!!!!")
                r.pause_threshold=1
                audio = r.listen(source)
        try:
                print("Recognising....")
                query= r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")

        except Exception as e:
               # print(e)

            print("Please dear say again..!!!!")
            return "None"
        return query

if __name__=="__main__" :
         wishMe()
         while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                           speak('Searching wikipedia...')
                           query=query.replace("wikipedia", "")
                           results=wikipedia.summary(query,sentence=2)
                           speak("According to wikipedia")
                           speak(results)