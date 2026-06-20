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

#targets for BLOSSOM equipment
target_fourth = (851, 498)
target_third = (852, 464)
target_second = (851, 429)
target_first = (851, 391)

#targets for PEST equipment
target_p1 = (850, 464)
target_p2 = (850, 428)
target_p3 = (852, 500)
target_p4 = (851, 392)

direction = input("which way are you starting? (up/down) ")
direction = direction.lower()
print("started")
held_keys = set()

#tolerance for pixels
def pixel_close(actual, target, tolerance=10):
    return (
        abs(actual[0] - target[0]) <= tolerance and
        abs(actual[1] - target[1]) <= tolerance and
        abs(actual[2] - target[2]) <= tolerance
    )

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

def find_blossom():
    x, y = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bBlue.png", confidence=0.75
    )
                    
    x2, y2 = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bChain.png", confidence=0.85
    )
                        
    x3, y3 = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bGlove.png", confidence=0.85
    )

    x4, y4 = pag.locateCenterOnScreen(
        r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\bNeck.png", confidence=0.85
    )
    return (x, y), (x2, y2), (x3, y3), (x4, y4)

def find_pest_equip():
    x, y = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pChain.png", confidence=0.85
    )
                
    x2, y2 = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pCloak.png", confidence=0.85
    )
                
    x3, y3 = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pGlove.png", confidence=0.85
    )
                
    x4, y4 = pag.locateCenterOnScreen(
    r"D:\Python Projects\Tests\Gardening-Mod\GardeningMod\Image recognition\pRing.png", confidence=0.85
    )
    return (x, y), (x2, y2), (x3, y3), (x4, y4)

mode = "sweeping"

def mod():
    print("running")
    #warp to garden spawn
    global mode, direction
    while True:
        # check if pests are about to spawn then swap to other equipment
        if pixel_close(pag.pixel(1369, 380), target_pests_spawns): 
            print("detected pests")
            mode = "pests"
            release_all()
            pag.press("capslock")
            time.sleep(0.3)
            p1, p2, p3, p4 = find_pest_equip()
            #if the equipment isnt where it should be, equip it
            if (p1) != target_p1:
                pag.moveTo(p1)
                time.sleep(0.1)

                pag.leftClick()
            if (p2) != target_p2:
                pag.moveTo(p2)
                time.sleep(0.1)
            
                pag.leftClick()
            if (p3) != target_p3:
                pag.moveTo(p3)
                time.sleep(0.1)
                
                pag.leftClick()

            if (p4) != target_p4:
                pag.moveTo(p4)
                time.sleep(0.1)
                
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
            mode = "sweeping"
        
        #if pests are spawned, go do all the stuff
        elif pixel_close(pag.pixel(1827, 384), target_pest2) or pixel_close(pag.pixel(1828, 384), target_pest2) or pixel_close(pag.pixel(1840, 384), target_pest2):
            print("detected pests spawned")
            mode = "pests"
            release_all()
            pag.press("capslock")
            time.sleep(0.5)
            b1, b2, b3, b4 = find_blossom()
            if (b2) != target_second:
                print("in place")
                pag.moveTo(b2)
                time.sleep(0.1)
                
                pag.leftClick()
            if (b1) != target_first:
                pag.moveTo(b1)
                time.sleep(0.1)
                
                pag.leftClick()
            if (b3) != target_third:
                pag.moveTo(b3)
                time.sleep(0.1)
                
                pag.leftClick()

            if (b4) != target_fourth:
                pag.moveTo(b4)
                time.sleep(0.1)
                
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
            time.sleep(1)
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
        
        
        elif pixel_close(pag.pixel(1236, 359), target_lane_switch) and pixel_close(pag.pixel(723, 371), target_lane_switch):
            print("changing lane")
            mode = "change lane"
        
        elif mode == "sweeping":
            print("sweeping")
            if direction == "up":
              hold("d")
              hold("space")
              
            
            elif direction == "down":
                print("down")
                hold("s")
                hold("space")

        elif mode == "change lane":
            print("changing lane")
            release_all()
            if direction == "up":
                hold("w")
                time.sleep(0.4)
                release("w")
                direction = "down"
                mode = "sweeping"
            
            elif direction == "down":
                hold("a")
                time.sleep(0.4)
                release("a")
                direction = "up"
                mode = "sweeping"

        elif kb.is_pressed("esc"):
            release_all()
            break




kb.add_hotkey("esc", emergency_stop)
kb.add_hotkey("7", mod)
kb.wait()
