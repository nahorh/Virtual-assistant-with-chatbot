import speech_recognition as sr
import pyttsx3
from talk import talk,talkG
engine=pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()



def listen():
    try:
        listener=sr.Recognizer()
        mic=sr.Microphone()
        talk('Speak now')
        with mic as source:
            listener.adjust_for_ambient_noise(source)
            # listener.pause_threshold=2
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice,language="en-In")
            cmd = cmd.lower()
            return cmd
            # if 'alexa' in cmd:
            #     cmd = cmd.replace('alexa', '')
            #     print(cmd)
            # else:
            #     cmd=''
            #     speak("Sorry, did you speak to me?")
    except sr.UnknownValueError:
        pass
        # print("Failed to listen")
        # speak("This type of voice can't be converted to text.")
        # listen()
    except sr.RequestError:
        talk("Please check you internet connection.")