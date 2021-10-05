import os
# from pynput import keyboard,mouse
import mouse
from pynput.keyboard import Key,Controller
# from pynput.mouse import Button,Controller
from time import sleep
# mouse=Controller()
keyboard=Controller()

def openChrome():
    os.system('start chrome.exe')

def openNotepad():
    os.system("start notepad.exe")

def openWord():
    os.system("start winword")

def showAllDesktops():
    keyboard.press(Key.cmd_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)   
    keyboard.release(Key.cmd_l)   

def escape():
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def showDesktop():
    keyboard.press(Key.cmd_l)
    keyboard.press('d')
    keyboard.release('d')
    keyboard.release(Key.cmd_l)

def openSettings():
    keyboard.press(Key.cmd_l)
    keyboard.press('i')
    keyboard.release(Key.cmd_l)
    keyboard.release('i')

def emojiKeyboard():
    keyboard.press(Key.cmd_l)
    keyboard.press('.')
    keyboard.release(Key.cmd_l)
    keyboard.release('.')

def takeScreenShot():
    keyboard.press(Key.cmd_l)
    keyboard.press(Key.shift_l)
    keyboard.press('s')
    keyboard.release(Key.cmd_l)
    keyboard.release(Key.shift_l)
    keyboard.release('s')
    sleep(5)
    for i in range(4):
        keyboard.press(Key.tab)                     

        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    openActionCenter()              



def openActionCenter():
    keyboard.press(Key.cmd_l)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.cmd_l)

def openProjectorSettings():
    keyboard.press(Key.cmd_l)
    keyboard.press('p')
    keyboard.release(Key.cmd_l)
    keyboard.release('p')

def createNewDesktop():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.cmd_l)
    keyboard.press()

def showBluetoothDevices():
    keyboard.press(Key.cmd_l)
    keyboard.press('k')
    keyboard.release('k')
    keyboard.release(Key.cmd_l)

def showClipboard():
    keyboard.press(Key.cmd_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.cmd_l)

def openMagnifier():
    keyboard.press(Key.cmd_l)
    keyboard.press('=')
    keyboard.release('=')
    keyboard.release(Key.cmd_l)

def copy():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def paste():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)