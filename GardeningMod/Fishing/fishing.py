import time
import os
import pyautogui as pag
import keyboard as kb

#target values of colour and of location of the pixel
target_red =
red = 

#add a tolerance for rgb values
def pixel_close(actual, target, tolerance=10):
    return (
        abs(actual[0] - target[0]) <= tolerance and
        abs(actual[1] - target[1]) <= tolerance and
        abs(actual[2] - target[2]) <= tolerance
    )


#main function that will detect the pixel and if it turns the colour, it will fish, otherwise it will do nothing
def fish():
  global red, target_red
  while True:
    if pixel_close(pag.pixel(red), target_red):
      pag.click(button="right")
      time.sleep(0.1)
      pag.press("1")
      time.sleep(0.1)
      pag.click(button="right")
      time.sleep(0.1)
      pag.press("4")
      pag.click(button="right")
      time.sleep(0.1)

  kb.add_hotkey("8", fish)
