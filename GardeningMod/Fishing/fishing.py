import time
import os
import pyautogui as pag
import keyboard as kb
import random
import numpy as np
# Source - https://stackoverflow.com/a/58043888
# Posted by Emerson
# Retrieved 2026-06-22, License - CC BY-SA 4.0

import pynput
mouse = pynput.mouse.Controller()



#target values of colour and of location of the pixel
target_red = 255, 85, 85

#add a tolerance for rgb values
def pixel_close(actual, target, tolerance=10):
    return (
        abs(actual[0] - target[0]) <= tolerance and
        abs(actual[1] - target[1]) <= tolerance and
        abs(actual[2] - target[2]) <= tolerance
    )

# Source - https://stackoverflow.com/a/58043888
# Posted by Emerson
# Retrieved 2026-06-22, License - CC BY-SA 4.0



def move_smooth(xm, ym, t):
    last = 0

    for i in range(t):
        progress = i / (t - 1)

        smooth = progress * progress * (3 - 2 * progress)

        step = smooth - last
        last = smooth

        jitter_x = random.uniform(-0.15, 0.15)
        jitter_y = random.uniform(-0.15, 0.15)

        mouse.move(
            step * xm + jitter_x,
            step * ym + jitter_y
        )

        time.sleep(random.uniform(0.012, 0.020))
        




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


#function for moving mouse too
def lava():
  print("Lava fishing")
  global red, target_red
  while True:
    up = random.randint(-700, -350)
    down = -500 - up
    left = random.randrange(-20, 20, 2)
    right1 = (0 - left)//2
    time_sleep = random.randrange(5, 15)/100
    
    if pixel_close(pag.pixel(1012, 573), target_red):
      time.sleep(time_sleep)
      pag.click(button="right")
      time.sleep(time_sleep)
      move_smooth(0, 540, random.randrange(5, 12))
      pag.press("1")
      time.sleep(time_sleep)
      pag.click(button="right")
      time.sleep(time_sleep)
      pag.click(button="right")
      time.sleep(time_sleep)
      pag.click(button="right")
      time.sleep(0.1)
      print("Moving up")
      move_smooth(40, up, random.randrange(11, 23))
      time.sleep(time_sleep + 0.2)
      move_smooth(-20, down, random.randrange(3, 10))
      pag.press("4")
      pag.click(button="right")
      time.sleep(0.1)

    if kb.is_pressed("esc"):
      print("Stopping.")
      break


def trophy():
  print("Trophy Fishing")
  global red, target_red
  while True:
    if pixel_close(pag.pixel(1012, 573), target_red):
      pag.click(button="right")
      time.sleep(random.randrange(5, 20)/100)
      pag.click(button="right")
    if kb.is_pressed("esc"):
       print("Stopping.")
       break

kb.add_hotkey("8", fish)
kb.add_hotkey("7", lava)
kb.add_hotkey("6", trophy)
kb.wait()