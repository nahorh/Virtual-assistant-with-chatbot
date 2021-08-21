import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

possibilities=['swim','bike','run','laugh']
def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            # if 'alexa' in cmd:
            #     cmd = cmd.replace('alexa', '')
            #     print(cmd)
            # else:
            #     cmd=''
            #     speak("Sorry, did you speak to me?")
    except:
        print("Failed to listen")
        speak("Something went wrong on the internet. Could you please speak again?")
        listen()
    return cmd

def GetSpeech():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice,language='en-In')
            cmd = cmd.lower()
    except:
        print("Failed to listen")
        speak("Something went wrong on the internet. Could you please speak again?")
        GetSpeech()
    return cmd

def run_alexa():
    speak("Listening")
    cmd = str(listen())
    # cmd="send a whatsapp message"
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date=datetime.datetime.date
        speak('Current time is ' + time)
    elif 'date' in cmd:
        date=str(datetime.datetime.now().date())
        speak("Today's date is "+date)
    elif 'day' in cmd:
        days=str(datetime.datetime.today().weekday())
        Days1={"0":"monday","1":"tuesday","2":"wednesday","3":"thursday","4":"friday","5":"saturday","6":"sunday"}
        whichDay=Days1[days]
        speak("Today is "+whichDay)
    elif 'who is' in cmd:
        person = cmd.replace('who the heck is', '')
        information = wikipedia.summary(person, 1)
        print(information)
        speak(information)
    elif 'who invented ' in cmd:
        information=wikipedia.summary(cmd,1)
        speak(information)
    elif 'send a whatsapp message' in cmd:
        speak("Okay")
        SendWhatsAppMsg()
    elif 'are you single' in cmd:
        speak('I am in a relationship with wifi')
    elif 'joke' in cmd:
        speak(pyjokes.get_joke())
    elif 'when' in cmd:
        instance=wikipedia.summary(cmd,1)
        print(instance)
        speak(instance)
    elif 'thank you' in cmd:
        speak("You're welcome anytime.")
    elif 'what is' in cmd:
        information=wikipedia.summary(cmd,1)
        speak(information)
    elif 'what can you do ' in cmd:
        speak("I can send a message for you on whatsapp, an email on the internet and also browse for information you need")
    elif 'can you':
        pass
    else:
        information=wikipedia.summary(cmd,1)
        speak("This is what I found on the internet"+information)


def SendWhatsAppMsg():
    file=open("contacts.json")
    contacts=file.read()
    file.close()
    contacts=json.loads(contacts)
    speak("To whom you want to send message")
    # msgToBeSentTo=GetSpeech()
    msgToBeSentTo="kaka"
    msgToBeSentTo=msgToBeSentTo.replace('to','')
    msgToBeSentTo=str(msgToBeSentTo.title())#the name of the contact to which message is to be delivered
    try:
        number=contacts[msgToBeSentTo]
        number="+91"+number
        print(number)
        speak(f"{msgToBeSentTo} found in your saved contacts list")
        speak("Please tell me the message that i shall write.")
        message=str(GetSpeech())
        pywhatkit.sendwhatmsg_instantly(number,message)
    except Exception as e:
        print("The number could not be found. ",e)
        speak("Sorry, i couldnt find the contact in the contacts list")

while 1:
    run_alexa()

