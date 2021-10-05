import pyttsx3 as tts
from gtts import gTTS
# from playsound import playsound
import os
from playsound import playsound

engine=tts.init()
voices=engine.getProperty('voices')
engine.setProperty('vocie',voices[0].id)
engine.setProperty('rate',140)

# engine.say("HEllo  rohan i am your bot")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talkG(text):
    engine=gTTS(text=text,slow=False,lang='hi')
    engine.save('tts.mp3')
    playsound('tts.mp3')
    

# talk('please tell me the message that i shall write')