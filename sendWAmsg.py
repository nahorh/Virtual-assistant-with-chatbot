import json
import pyttsx3
# import speech_recognition as sr
import pywhatkit as pwt
import pyautogui as pag
from talk import talkG,talk
import speechRecognize as sr
# listener=sr.Recognizer()
# mic=sr.Microphone()

# def listen():
#     counter=0
#     try:
#         with mic as source:
#             listener.adjust_for_ambient_noise(source)
#             listener.pause_threshold=1
#             voice = listener.listen(source)
#             cmd = listener.recognize_google(voice,language="en-In")
#             cmd = cmd.lower()
#             return cmd
#     except sr.UnknownValueError:
#         if counter<3:
#             print("Did not understand the speech.")
#             speak("Sorry, I didn't understand what you said. Please speak again.")
#         else:
#
#             speak('Sorry, please try again later.')
#     except sr.RequestError:
#         print('Internet connection error.')
#         speak("I am facing issues while connecting to the internet. Please try again in some time.")

# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def SendWhatsAppMsg():
    file=open("contacts.json")
    contacts=file.read()
    file.close()
    contacts=json.loads(contacts)
    talk("To whom you want to send message")
    msgToBeSentTo=sr.listen()
    # msgToBeSentTo="kaka"
    msgToBeSentTo=msgToBeSentTo.replace('to ','')
    msgToBeSentTo=str(msgToBeSentTo.title()) #the name of the contact to which message is to be delivered
    try:
        number=contacts[msgToBeSentTo]
        number=str(number)
        number="+91"+number
        number=str(number)
        print(number)
        talk(f"{msgToBeSentTo} found in your saved contacts list")
        talk("Please tell me the message that i shall write.")
        message=sr.listen()
        message=str(message)
        pwt.sendwhatmsg_instantly(number,message)
        # sleep(10)
        talk("Code resumed")
        try:
            print('Trying to click')
            mousePosition=pag.locateCenterOnScreen("send_button.png",confidence=0.9)
            pag.moveTo(mousePosition[0:2])
            pag.click()
        except:
            print('couldnt click')
            pass
    except Exception as e:
        print("The number could not be found. ",e)
        talk("Sorry, i couldnt find the contact in the contacts list")

def sendDirectMessage(number,message):
    pwt.sendwhatmsg_instantly(number,message)
    try:
            mousePosition=pag.locateCenterOnScreen("send_button.png",confidence=0.9)
            pag.moveTo(mousePosition[0:2])
            pag.click()
    except:
        pass


def activateChatbot():
    sendDirectMessage('+14155238886','join no-plenty')

def deactivateChatbot():
    sendDirectMessage('+14155238886','stop')