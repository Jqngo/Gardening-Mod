import time
import pyautogui as pag
import keyboard as kb

pestscoords = 91, 936

targetPests = (0, 168, 0)


held_keys = set()

def hold(key): #held key is added to a set
    pag.keyDown(key)
    held_keys.add(key)

def release(key): # release function 
    pag.keyUp(key)
    held_keys.discard(key)

def release_all():
    for key in held_keys.copy():
        pag.keyUp(key)
    held_keys.clear()


def mod():
    #warp to garden spawn
    while True:

        if pag.pixel(91, 936) == targetPests:   #if pests are spawned, go do all the stuff
            release_all()
            
            time.sleep(0.1)
            pag.press("b")
            time.sleep(0.05)
            pag.press("n")
            time.sleep(1)
            pag.press("4")
            time.sleep(0.25)
            pag.mouseDown(button = "right")
            time.sleep(5)
            pag.mouseUp(button = "right")
            pag.press("h")
        
        elif # going up a lane, going down a lane,


kb.add_hotkey("esc", release_all)
kb.wait()
