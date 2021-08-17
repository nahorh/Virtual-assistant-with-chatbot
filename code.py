import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

possibilities=['swim','bike','run','laugh']
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('listening')
            print('I am listening to your voice...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                command='thank you'
                talk("Sorry, did you speak to me?")
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date=datetime.datetime.date
        talk('Current time is ' + time)
        
        talk(date)
    elif 'day is today' in command:
        days=str(datetime.date.day)
        Days1={"1":"monday","2":"tuesday","3":"wednesday","4":"thursday","5":"friday","6":"saturday","7":"sunday"}
        whichDay=Days1[days]
        talk(whichDay)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who invented ' in command:
        info=wikipedia.summary(command,1)
        talk(info)
    elif 'date' in command:
        date=str(datetime.datetime.now().date())
        talk("Today's date is "+date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'when' in command:
        instance=wikipedia.summary(command,1)
        print(instance)
        talk(instance)
    elif 'thank you' in command:
        talk("You're welcome anytime.")
    elif 'what is' in command:
        info=wikipedia.summary(command,1)
        talk(info)
    elif 'what can you do ' in command:
        talk("I can send a message for you on whatsapp, an email on the internet and also browse for information you need")
    elif 'can you':
        pass
    else:
        info=wikipedia.summary(command,1)
        talk("This is what I found on the internet"+info)

while 1:
    run_alexa()
