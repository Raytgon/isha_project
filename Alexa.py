import speech_recognition as sr
import pyttsx3
import pywhatkit
import  wikipedia
import pyjokes
import datetime
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say('How can i help you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("start speaking")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is'+time)
        print(time)
    elif 'who is' in command:
        search=command.replace('who is','')
        info=wikipedia.summary(search,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'how are you' in command:
        talk('i am great')
    elif 'exit'or'bye' in command:
        quit


while True:
    run_alexa()