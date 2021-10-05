import sendWAmsg as swam
import openApps as oa
import webbrowser as wb
from datetime import datetime
from talk import talk, talkG
import sendEmail
import weather

commandsList = ['send a whatsapp message',
                'activate start the chatbot',
                'deactivate stop the chatbot',
                'open start youtube',
                'what is tell me todays the date',
                'what is tell me todays the day',
                'open start google chrome',
                'open start notepad'
                'open start word',
                'show all view all desktops desktop',
                'press escape key',
                'go to show view desktop',
                'go to open settings',
                'show open view emoji keyboard',
                'take screenshot',
                'go to open action center centre',
                'show open view projector settings',
                'make create new desktop',
                'show view open bluetooth devices',
                'show view open clipboard',
                'start open magnifier',
                'copy this text area',
                'paste the text it here',
                'send an a email',
                'tell me the weather of',
                'what is tell me the time',
                'stop listening to me',
                ]


def perform(i, cmd):
    if i == 0:
        swam.SendWhatsAppMsg()
    elif i == 1:
        swam.activateChatbot()
    elif i == 2:
        swam.deactivateChatbot()
    elif i == 3:
        wb.open_new_tab('www.youtube.com')
    elif i == 4:
        talk(f'todays date is {datetime.now().date()}')
    elif i == 5:
        day = datetime.now().weekday()
        days = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}
        day = days[day]
        talk(f'today is {day}')
    elif i == 6:
        oa.openChrome()
    elif i == 7:
        oa.openWord()
    elif i == 8:
        oa.openWord()
    elif i == 9:
        oa.showAllDesktops()
    elif i == 10:
        oa.escape()
    elif i == 11:
        oa.openSettings()
    elif i == 12:
        oa.emojiKeyboard()
    elif i == 13:
        oa.takeScreenShot()
    elif i == 14:
        oa.openActionCenter()
    elif i == 15:
        oa.openProjectorSettings()
    elif i == 16:
        oa.createNewDesktop()
    elif i == 17:
        oa.showBluetoothDevices()
    elif i == 18:
        oa.showClipboard()
    elif i == 19:
        oa.openMagnifier()
    elif i == 20:
        oa.copy()
    elif i == 21:
        oa.paste()
    elif i == 22:
        sendEmail.get_email_info()
    elif i == 23:
        weather.getWeather(cmd)
    elif i == 24:
        talk('current time is')
        t = datetime.now().time().strftime('%I:%M%p')
        talk(t)
    elif i == 25:
        print('Stop listening to me executed')
        talk('Okay, bye. see you soon')
        exit(0)
    elif i == 'None':
        pass
    # dict1={'send a whatsapp message':swam.SendWhatsAppMsg(),
    #             'activate start the chatbot':swam.activateChatbot(),
    #             'deactivate stop the chatbot':swam.deactivateChatbot(),
    #             'open start youtube':wb.open_new_tab('www.youtube.com'),
    #             'what is tell me todays the date':datetime.now().date(),
    #             'what is tell me todays the day':datetime.now().time().strftime('%I%M%p'),
    #             'open start google chrome':oa.openChrome(),
    #             'open start notepad':oa.openNotepad(),
    #             'open start microsoft ms word':oa.openWord(),
    #             'show all view all desktops desktop':oa.oa.showAllDesktops(),
    #             'press escape key':oa.escape(),
    #             'go to show view desktop':oa.showDesktop(),
    #             'go to open settings':oa.openSettings(),
    #             'show open view emoji keyboard':oa.emojiKeyboard(),
    #             'take screenshot':oa.takeScreenShot(),
    #             'go to open action center centre':oa.openActionCenter(),
    #             'show open view projector settings':oa.openProjectorSettings(),
    #             'make create new desktop':oa.createNewDesktop(),
    #             'show view open bluetooth devices':oa.showBluetoothDevices(),
    #             'show view open clipboard':oa.showClipboard(),
    #             'start open magnifier':oa.openMagnifier(),
    #             'copy this text area':oa.copy(),
    #             'paste the text it here':oa.paste(),
    #             'stop dont listen listening to me':print('Code exit() called')
    #             }
    # def func1():
    #     print('func 1 called')
    # sampledict={'str1':func1,'str2':'func2'}
    # sampledict['str1']
    # perform['show open view emoji keyboard']
    # perform()

    # length=len(commandsList)
    # perform(0)

    # list=[swam.SendWhatsAppMsg(),
    #          swam.activateChatbot(),
    #          swam.deactivateChatbot(),
    #          wb.open_new_tab('www.youtube.com'),
    #          talk(f'todays date is {datetime.now().date()}'),
    #          talk(f'today is {datetime.now().weekday()}'),
    #          oa.openChrome(),
    #          oa.openNotepad(),
    #          oa.openWord(),
    #          oa.showAllDesktops(),
    #          oa.escape(),
    #          oa.showDesktop(),
    #          oa.openSettings(),
    #          oa.emojiKeyboard(),
    #          oa.takeScreenShot(),
    #          oa.openActionCenter(),
    #          oa.openProjectorSettings(),
    #          oa.createNewDesktop(),
    #          oa.showBluetoothDevices(),
    #          oa.showClipboard(),
    #          oa.openMagnifier(),
    #          oa.copy(),
    #          oa.paste(),
    #          print('Stop exit() called')
    # ]
