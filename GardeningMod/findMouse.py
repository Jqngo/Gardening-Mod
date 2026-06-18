import time
import pyautogui as pag
import keyboard as kb





def getCoordinates():
    print(pag.position())

kb.add_hotkey("l", getCoordinates)

print("press l to get coordinates")

kb.wait()