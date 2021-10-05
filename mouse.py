# from pynput import mouse,keyboard
from pynput.mouse import Button,Controller

mouse=Controller()

def leftClick():
    mouse.click(Button.left,1)

def rightClick():
    mouse.click(Button.right, 1)

def doubleClick():
    mouse.click(Button.left,2)
