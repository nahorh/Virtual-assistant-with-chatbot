import mouse
import fuzzyMatch as fm
import openApps as oa
# import sendWAmsg as swam
import speechRecognize as sr
from pynput.keyboard import Controller, Key
from talk import talk, talkG
from commnads import commandsList, perform

# import commnads

toBePerformed = len(commandsList) - 1


# talk('I m awake!')
def Assistant():
    text = sr.listen()
    commandFound = False
    print(text)
    for i in range(len(commandsList)):
        if (fm.match(commandsList[i], text)):
            toBePerformed = i
            commandFound = True
            break
    if commandFound:
        print('Pass')
        perform(toBePerformed, text)
        # print(toBePerformed,'is to be performed i guess')

    else:
        talk("I couldn't understand that.")


print('called')
# while 1:
#   Assistant()
