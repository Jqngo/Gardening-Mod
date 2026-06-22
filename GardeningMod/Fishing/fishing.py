import time
import os
import pyautogui as pag
import keyboard as kb

#target values of colour and of location of the pixel
target_red = 255, 85, 85

#add a tolerance for rgb values
def pixel_close(actual, target, tolerance=10):
    return (
        abs(actual[0] - target[0]) <= tolerance and
        abs(actual[1] - target[1]) <= tolerance and
        abs(actual[2] - target[2]) <= tolerance
    )


#main function that will detect the pixel and if it turns the colour, it will fish, otherwise it will do nothing
def fish():
  print("Fishing")
  global red, target_red
  while True:
    if pixel_close(pag.pixel(1012, 573), target_red):
      pag.click(button="right")
      time.sleep(0.1)
      pag.press("1")
      time.sleep(0.1)
      pag.click(button="right")
      time.sleep(0.1)
      pag.press("4")
      pag.click(button="right")
      time.sleep(0.1)
    
    if kb.is_pressed("esc"):
       print("Stopping.")
       break

kb.add_hotkey("8", fish)
kb.wait()
