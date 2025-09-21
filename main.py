import time

import pyautogui

from Atlas_Functions import *
from keyword import *
time.sleep(5)
#Sreen_Sot()

if pyautogui.locateOnScreen(r'Atlas_img/Spin.png'):
    print('t')
time.sleep(5)
Del = pyautogui.locateOnScreen(r'Atlas_img/DEL.png')
# x, y
#pyautogui.moveTo(2850, 1169)
#time.sleep(1)
#pyautogui.mouseDown()
#pyautogui.drag(0, -300, 1, button='left')
#pyautogui.mouseUp()

for x in range(2):
    pyautogui.moveTo(2850, 1169)
    time.sleep(1)
    pyautogui.drag(0, -300, 1, button='left')
    x + 1




