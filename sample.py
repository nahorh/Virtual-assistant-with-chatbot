# # from gtts import gTTS
# # import os
# # from playsound import playsound
# # from time import sleep
# # txt="hello how are you"
# # speech=gTTS(text=txt,slow=False,lang='en-In')
# # speech.save('voice.mp3')
# # sleep(2)
# # playsound('A:\\\\mitwpu\\\\ty\\\\tri 1\\\\Hardware Maintainance and Programming Skills for Electronics Software\\\\Grp Project\\\\virtual assistant\\\\sample\\\\voice.mp3')

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# # for voice in voices:
# #     print("Voice:")
# #     print(" - ID: %s" % voice.id)
# #     print(" - Name: %s" % voice.name)
# #     print(" - Languages: %s" % voice.languages)
# #     print(" - Gender: %s" % voice.gender)
# #     print(" - Age: %s" % voice.age)

# def get_email_info():
#     talk('To Whom you want to send email')
#     name = get_info()
#     receiver = email_list[name]
#     print(receiver)
#     talk('What is the subject of your email?')
#     subject = get_info()
#     talk('Tell me the text in your email')
#     message = get_info()
#     send_email(receiver, subject, message)
#     talk('Hey lazy ass. Your email is sent')
#     talk('Do you want to send more email?')
#     send_more = get_info()
#     if 'yes' in send_more:
#         get_email_info()

# send_email("receiver","Sample email","Hello this is an email from python.")



# # code for image recognition of whatsapp send button clicking
# import pywhatkit as pwt
# import pyautogui as pag
# from pynput import mouse,keyboard
# from pynput.mouse import Controller,Button
# from pynput.keyboard import Controller,Key
# from time import sleep
# mouse=Controller()
# keyboard=Controller()
# sleep(5)
# mousePosition=pag.locateCenterOnScreen("send_button.png",confidence=0.9)
# pag.moveTo(mousePosition[0:2])
# pag.click()



# import os
# from pynput import mouse,keyboard
# from pynput.mouse import Controller,Button
# from pynput.keyboard import Controller,Key
# from time import sleep
# mouse=Controller()
# keyboard=Controller()
# os.system("start chrome.exe")
# sleep(3)
# # keyboard.release(Key.f6)
# # sleep(1)
# keyboard.type("web.whatsapp.com")
# keyboard.press(Key.enter)


# sending whatsapp message instantly
# from time import sleep
# import pywhatkit as pwk
# import pyttsx3
# import pyautogui as pag
# from pynput import keyboard
# from pynput.keyboard import Controller,Key
# import webbrowser
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# keyboard=Controller()
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
# talk("Hello")
# pwk.sendwhatmsg_instantly("+918983117939","Hi")
# talk("Code resumed")
# mousePosition=pag.locateCenterOnScreen("send_button.png",confidence=0.9)
# pag.moveTo(mousePosition[0:2])
# pag.leftClick()
# sleep(2)
# keyboard.press(Key.ctrl)
# keyboard.press('w')
# keyboard.release('w')

# keyboard.release(Key.ctrl)



from time import sleep
import speech_recognition as sr
import pyautogui as pag
# from pynput import mouse,keyboard
# from pynput.mouse import Button,Controller
# from pynput.keyboard import Key,Controller
import pyttsx3
import pywhatkit as pwt
import datetime
import wikipedia
import pyjokes
# import json

import webbrowser
import os
from pynput import mouse,keyboard
from pynput.mouse import Controller,Button
from pynput.keyboard import Controller,Key
# from time import sleep
# import pyautogui as pt
mouse=Controller()
keyboard=Controller()
import openApps as oa
import sendWAmsg as swam
import fuzzyMatch as fm
from talk import talk
# def openChrome():
#     os.system('start chrome.exe')

# def openNotepad():
#     os.system("start notepad.exe")

# def openWord():
#     os.system("start winword")

# def showAllDesktops():
#     keyboard.press(Key.cmd_l)
#     keyboard.press(Key.tab)
#     keyboard.release(Key.tab)   
#     keyboard.release(Key.cmd_l)   

# def escape():
#     keyboard.press(Key.esc)
#     keyboard.release(Key.esc)

# def showDesktop():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('d')
#     keyboard.release('d')
#     keyboard.release(Key.cmd_l)

# def openSettings():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('i')
#     keyboard.release(Key.cmd_l)
#     keyboard.release('i')

# def emojiKeyboard():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('.')
#     keyboard.release(Key.cmd_l)
#     keyboard.release('.')

# def takeScreenShot():
#     keyboard.press(Key.cmd_l)
#     keyboard.press(Key.shift_l)
#     keyboard.press('s')
#     keyboard.release(Key.cmd_l)
#     keyboard.release(Key.shift_l)
#     keyboard.release('s')
#     sleep(5)
#     for i in range(4):
#         keyboard.press(Key.tab)                     

#         keyboard.release(Key.tab)
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     sleep(1)
#     openActionCenter()              



# def openActionCenter():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('a')
#     keyboard.release('a')
#     keyboard.release(Key.cmd_l)

# def openProjectorSettings():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('p')
#     keyboard.release(Key.cmd_l)
#     keyboard.release('p')

# def createNewDesktop():
#     keyboard.press(Key.ctrl)
#     keyboard.press(Key.cmd_l)
#     keyboard.press()

# def showBluetoothDevices():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('k')
#     keyboard.release('k')
#     keyboard.release(Key.cmd_l)

# def showClipboard():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('v')
#     keyboard.release('v')
#     keyboard.release(Key.cmd_l)

# def openMagnifier():
#     keyboard.press(Key.cmd_l)
#     keyboard.press('=')
#     keyboard.release('=')
#     keyboard.release(Key.cmd_l)

# def copy():
#     keyboard.press(Key.ctrl)
#     keyboard.press('c')
#     keyboard.release('c')
#     keyboard.release(Key.ctrl)

# def paste():
#     keyboard.press(Key.ctrl)
#     keyboard.press('v')
#     keyboard.release('v')
#     keyboard.release(Key.ctrl)
# openChrome()
# openNotepad()
# showAllDesktops()
# sleep(2)
# escape()

# showDesktop()
# openSettings()
# emojiKeyboard()
# takeScreenShot()
# openActionCenter()
# openProjectorSettings()
# showBluetoothDevices()
# showClipboard()
# openMagnifier()











# from time import sleep
# import speech_recognition as sr
# import pyautogui as pag
# from pynput import mouse,keyboard
# from pynput.mouse import Button,Controller
# from pynput.keyboard import Key,Controller
# import pyttsx3
# import pywhatkit as pwt
# import datetime
# import wikipedia
# import pyjokes
# import json

# listener = sr.Recognizer()
# # listener.energy_threshold=1000
# mic=sr.Microphone()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty()

# possibilities=['swim','bike','run','laugh']
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     try:
#         with mic as source:
#             listener.adjust_for_ambient_noise(source)
#             listener.pause_threshold=1
#             voice = listener.listen(source)
#             cmd = listener.recognize_ibm(voice,language="en-In")
#             cmd = cmd.lower()
#             return cmd
#             # if 'alexa' in cmd:
#             #     cmd = cmd.replace('alexa', '')
#             #     print(cmd)
#             # else:
#             #     cmd=''
#             #     talk("Sorry, did you talk to me?")
#     except sr.UnknownValueError:
#         print("Failed to listen")
#         talk("This type of voice can't be converted to text.")
#         # listen()
#     except sr.RequestError:
#         talk("Your internet connectivity is poor.")
        # listen()
    # except sr.WaitTimeoutError:
    #     talk("You did not say anything")

# def GetSpeech():
#     try:
#         with mic as source:
#             # listener.adjust_for_ambient_noise(source)
#             voice = listener.listen(source,timeout=5)
#             cmd = listener.recognize_google(voice,language='en-In')
#             cmd = cmd.lower()
#             return cmd
#     except sr.UnknownValueError:
#         print("Cannot convert this voice to text")
#         talk("This type of voice can't be converted to text.")
#         # listen()
#     except sr.RequestError:
#         talk("Your internet connectivity is poor.")
#         talk("Please check your internet connection.")

def voiceAssistan():
    talk("Listening")
    cmd = str(listen())
    # cmd="send a whatsapp message"
    print("You said:\n"+cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        talk('playing ' + song)
        pwt.playonyt(song)
    elif 'open youtube' in cmd:
        webbrowser.open_new_tab("www.youtube.com")
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date=datetime.datetime.date
        talk('Current time is ' + time)
    elif 'date' in cmd:
        date=str(datetime.datetime.now().date())
        talk("Today's date is "+date)
    elif 'day' in cmd:
        days=str(datetime.datetime.today().weekday())
        Days1={"0":"monday","1":"tuesday","2":"wednesday","3":"thursday","4":"friday","5":"saturday","6":"sunday"}
        whichDay=Days1[days]
        talk("Today is "+whichDay)
    # elif 'who is' in cmd:
    #     person = cmd.replace('who the heck is', '')
    #     information = wikipedia.summary(person, 1)
    #     print(information)
    #     talk(information)
    # elif 'who invented ' in cmd:
    #     information=wikipedia.summary(cmd,1)
    #     talk(information)
    elif 'send a whatsapp message' in cmd:
        talk("Okay")
        swam.SendWhatsAppMsg()
    elif 'joke' in cmd:
        talk(pyjokes.get_joke())
    elif 'when' in cmd:
        instance=wikipedia.summary(cmd,4)
        print(instance)
        talk(instance)
    elif 'thank you' in cmd:
        talk("You're welcome anytime.")
    elif 'what is' in cmd:
        information=wikipedia.summary(cmd,4)
        talk(information)
    elif 'what can you do' in cmd:
        talk("I can send a message for you on whatsapp, an email on the internet and also browse for information you need")
    elif 'open chrome' in cmd:
        oa.openChrome()
    elif 'open notepad' in cmd:
        oa.openNotepad()
    elif 'open word' in cmd:
        oa.openWord()
    elif 'overview' in cmd:
        oa.showAllDesktops()
    elif 'escape key' in cmd:
        oa.escape()
    elif 'go to desktop' in cmd:
        oa.showDesktop()
    elif 'open settings' in cmd:
        oa.openSettings()
    elif 'open emoji keyboard' in cmd:
        oa.emojiKeyboard()
    elif 'take screenshot' in cmd:
        oa.takeScreenShot()
    elif 'open action centre' in cmd:
        oa.openActionCenter()
    elif 'open projector settings' in cmd:
        oa.openProjectorSettings()
    elif 'create new desktop' in cmd:
        oa.createNewDesktop()
    elif 'show bluetooth devices' in cmd:
        oa.showBluetoothDevices()
    elif 'open clipboard' in cmd:
        oa.showClipboard()
    elif 'open magnifier' in cmd:
        oa.openMagnifier()
    elif 'copy this' in cmd:
        oa.copy()
    elif 'paste' in cmd:
        oa.paste()
    elif 'stop listening to me' in cmd:
        print("Okay.")
        print("Thanks for speaking with me.")
        talk("Okay.")
        talk("Thanks for speaking with me.")
        exit()
    else:
        talk("I couldn't find anything related to that.")


# def SendWhatsAppMsg():
#     file=open("A:\\mitwpu\\ty\\tri 1\\Hardware Maintainance and Programming Skills for Electronics Software\\Grp Project\\virtual assistant\\sample\\contacts.json")
#     contacts=file.read()
#     file.close()
#     contacts=json.loads(contacts)
#     talk("To whom you want to send message")
#     msgToBeSentTo=GetSpeech()
#     # msgToBeSentTo="kaka"
#     msgToBeSentTo=msgToBeSentTo.replace('to ','')
#     msgToBeSentTo=str(msgToBeSentTo.title())#the name of the contact to which message is to be delivered
#     try:
#         number=contacts[msgToBeSentTo]
#         number=str(number)
#         number="+91"+number
#         number=str(number)
#         print(number)
#         talk(f"{msgToBeSentTo} found in your saved contacts list")
#         talk("Please tell me the message that i shall write.")
#         message=GetSpeech()
#         message=str(message)
#         pwt.sendwhatmsg_instantly(number,message)
#         # sleep(10)
#         talk("Code resumed")
#         try:
#             mousePosition=pag.locateCenterOnScreen("send_button.png",confidence=0.9)
#             pag.moveTo(mousePosition[0:2])
#             pag.click()
#         except:
#             pass
#     except Exception as e:
#         print("The number could not be found. ",e)
#         talk("Sorry, i couldnt find the contact in the contacts list")
# talk("Listening")

while 1:
#     print("Voice assistant reinitialized")
    voiceAssistan()





