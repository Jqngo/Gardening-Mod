import time
import os
import pyautogui as pag
import keyboard as kb

pestscoords = 91, 936

targetPests = (0, 168, 0)
target_pest2 = (170, 0, 0)
target_pests_spawns = (252, 84, 84)
target_pests_spawns2 = (85, 255, 85)
target_lane_switch = (255, 255, 85)
target_switch_error = (235, 221, 71)

direction = input("which way are you starting? (up/down) ")
print("started")
held_keys = set()

def emergency_stop():
    release_all()
    os._exit(0)

def hold(key): #held key is added to a set
    if key not in held_keys:
        pag.keyDown(key)
        held_keys.add(key)

def release(key): # release function 
    pag.keyUp(key)
    held_keys.discard(key)

def release_all(): # quick stop function
    for key in held_keys.copy():
        pag.keyUp(key)
    held_keys.clear()

mode = "sweeping"

def mod():
    #warp to garden spawn
    global mode, direction
    while True:
        
        if pag.pixel(1369, 380) == target_pests_spawns and pag.pixel(937, 186) == target_pests_spawns2 and pag.pixel(979, 184) == target_pests_spawns2: # check if pests are about to spawn then swap to other equipment
            mode = "pests"
            release_all()
            pag.press("capslock")
            time.sleep(0.1)
            x, y = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pChain.png", confidence=0.9
                )
            
            x2, y2 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pCloak.png", confidence=0.9
                )
            
            x3, y3 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pGlove.png", confidence=0.9
                )
            
            x4, y4 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pRing.png", confidence=0.9
                )
            pag.moveTo(x4, y4)
            time.sleep(0.1)
            pag.moveTo(x4+1, y4+1)
            pag.leftClick()
            pag.moveTo(x2, y2)
            time.sleep(0.1)
            pag.moveTo(x2+1, y2+1)
            pag.leftClick()
            pag.moveTo(x, y)
            time.sleep(0.1)
            pag.moveTo(x+1, y+1)
            pag.leftClick()
            pag.moveTo(x3, y3)
            time.sleep(0.1)
            pag.moveTo(x3+1, y3+1)
            pag.leftClick()
            time.sleep(0.1)
            pag.press("tab")
            time.sleep(0.1)
            pag.press("v")
            time.sleep(0.1)
            pag.rightClick()
            time.sleep(0.1)
            pag.press("2")
            time.sleep(0.1)
            mode = "resume"
        

        elif pag.pixel(91, 936) == targetPests or pag.pixel(1827, 384) == target_pest2 or pag.pixel(1828, 384) == target_pest2:   #if pests are spawned, go do all the stuff
            mode = "pests"
            release_all()
            pag.press("capslock")
            time.sleep(0.5)
            x, y = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bBlue.png", confidence=0.9
                )
                    
            x2, y2 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bChain.png", confidence=0.9
                )
                    
            x3, y3 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bGlove.png", confidence=0.9
                )
                    
            x4, y4 = pag.locateCenterOnScreen(
                r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bNeck.png", confidence=0.9
                )
            pag.moveTo(x4, y4)
            time.sleep(0.1)
            pag.moveTo(x4+1, y4+1)
            pag.leftClick()
            pag.moveTo(x2, y2)
            time.sleep(0.1)
            pag.moveTo(x2+1, y2+1)
            pag.leftClick()
            pag.moveTo(x, y)
            time.sleep(0.1)
            pag.moveTo(x+1, y+1)
            pag.leftClick()
            pag.moveTo(x3, y3)
            time.sleep(0.1)
            pag.moveTo(x3+1, y3+1)
            pag.leftClick()
            pag.press("tab")
            time.sleep(0.1)
            time.sleep(0.1)
            pag.press("v")
            time.sleep(0.1)
            pag.rightClick()
            #now set spawn and tp to the pests
            pag.press("h") 
            time.sleep(0.05)
            pag.press("n") # teleported to pests
            time.sleep(1)
            pag.press("4")
            time.sleep(0.25)
            pag.mouseDown(button = "right")
            hold("w")
            time.sleep(0.25)
            release("w")
            time.sleep(1)
            time.sleep(3)
            time.sleep(1)
            pag.mouseUp(button = "right")
            pag.press("b")
            time.sleep(0.1)
            pag.press("v")
            time.sleep(0.1)
            pag.rightClick()
            time.sleep(0.1)
            pag.press("2")
            time.sleep(0.1)
            mode = "sweeping"
        
        
        elif pag.pixel(1236, 359) == target_lane_switch and pag.pixel(723, 371) == target_lane_switch or pag.pixel(1403, 957) == target_switch_error or pag.pixel(1373, 910) == target_switch_error:
            mode = "change lane"
        
        elif mode == "sweeping":
            if direction == "up":
              hold("d")
              hold("space")
              
            
            elif direction == "down":
                hold("s")
                hold("space")

        elif mode == "change lane":
            release_all()
            if direction == "up":
                hold("w")
                time.sleep(0.5)
                release("w")
                direction = "down"
                mode = "sweeping"
            
            elif direction == "down":
                hold("a")
                time.sleep(0.5)
                release("a")
                direction = "up"
                mode = "sweeping"

        elif kb.is_pressed("esc"):
            release_all()
            break




kb.add_hotkey("esc", emergency_stop)
kb.add_hotkey("7", mod)
kb.wait()
