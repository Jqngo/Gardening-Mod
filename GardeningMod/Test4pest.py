
import time
import pyautogui as pag
import keyboard as kb


def check_pests():
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

def swap_back():
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
    pag.press("n")
    time.sleep(1)
    pag.press("4")
    time.sleep(0.25)
    pag.mouseDown(button = "right")
    time.sleep(5)
    pag.mouseUp(button = "right")
    pag.press("b")
    time.sleep(0.1)
    pag.press("v")
    time.sleep(0.1)
    pag.rightClick()
    time.sleep(0.1)
    pag.press("2")
    time.sleep(0.1)


kb.add_hotkey("#", check_pests)
kb.add_hotkey("8", swap_back)
kb.wait()   