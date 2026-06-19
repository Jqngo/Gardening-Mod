import time
import pyautogui as pag
import keyboard as kb





def getCoordinates():
    print(pag.position())

kb.add_hotkey("alt", getCoordinates)

print("press alt to get coordinates")

kb.wait()
