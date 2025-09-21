from Atlas_Functions import *

loop = True
loop_count = 0

while loop == True:
    loop_count += 1
    print(f'Loop #{loop_count}')
    time.sleep(480)
    BS = False
    while BS == False:
        BS = pyautogui.locateOnScreen(r'Atlas_img/Blue_Stacks.png')
    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Blue_Stacks.png'))