import time
import os
from Img_Location import *
from datetime import datetime
x = 0
ss_c = 0
end_date = ('04-11-2022')


def Scheduled_Maintenance():
    sm = True
    while sm == True:
        if pyautogui.locateOnScreen(r'Atlas_img/Scheduled_Maintenance.png'):
            time.sleep(300)
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Scheduled_Maintenance.png'))
            Sreen_Sot()
            Reset_Game()
        else:
            Sreen_Sot()
            sm = False


def Fail(fail, froze):
    Sreen_Sot()
    if froze != 4:
        froze += 1
        print('Game Failed')
        Reset_Game()
        fail -= 1
        return fail, froze
    elif froze == 4:
        Sreen_Sot()
        if pyautogui.locateOnScreen(r'Atlas_img/Blue_X.png'):
            print('Closing Game')
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Blue_X.png'))
            close = False
            while close == False:
                close = pyautogui.locateOnScreen(r'Atlas_img/Red_Close.png')
            pyautogui.click(close)
            froze = 0
            fail = 0
            return froze, fail
        elif Game_Shortcut():
            print('Launching Game')
            pyautogui.doubleClick(Game_Shortcut())
            time.sleep(5)
            if pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png'):
                pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png'))
                print('Game Launched')
            froze = 0
            fail = 0
            return froze, fail


def Closing_Ad():
    time.sleep(5)
    closed = 0
    if pyautogui.locateOnScreen(r'Atlas_img/Unavailable_Ad.png'):
        # HEARSAY
        Reset_Game()
    elif pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'):
        pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'))
    else:
        time.sleep(25)
        c = 0
        ad_count_X = len(os.listdir(r'Ad/Close_Ad'))
        ad_count_S = len(os.listdir(r'Ad/Skip_Ad'))
        run = 0
        while closed != 2:
            c = 0
            time.sleep(10)
            test = 0
            r = 0
            print(f'Test Run: {run}')
            for l in range(ad_count_S):
                l += 1
                print(f"Testing S{l}")
                if pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(r'Atlas_img/Unavailable_Ad.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(fr'Ad/Skip_Ad/S{l}.png'):
                    pyautogui.click(pyautogui.locateOnScreen(fr'Ad/Skip_Ad/S{l}.png'))
                    closed = 2
                    print('Successful Skipped')
                    break

            for l in range(ad_count_X):
                test += 1
                l += 1
                print(f"Testing X{l}")
                if pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                    run = 2
                    print('Error')
                    break
                elif pyautogui.locateOnScreen(fr'Ad/Close_Ad/X{l}.png'):
                    pyautogui.click(pyautogui.locateOnScreen(fr'Ad/Close_Ad/X{l}.png'))
                    closed += 1
                    print('Successful Closed')
                    break
                else:
                    c += 1
            if c == test:
                if run == 2:
                    t = time.localtime()
                    t = time.strftime("%H:%M:%S", t)
                    print('Unable To Close Ad At ' + t)
                    Sreen_Sot()
                    time.sleep(1)
                    Reset_Game()
                    closed = 2
                else:
                    run += 1
            elif c != test:
                closed = 2

        time.sleep(1)



def Sreen_Sot():
    print('Taking Screen Shot')
    ss = pyautogui.screenshot()
    date = datetime.now()
    date = date.strftime('%m-%d-%Y')
    t = time.localtime()
    t = time.strftime("%H.%M.%S", t)
    ss.save(fr'Screen_Shots\{date}({t}).png')
    print('Screen Shot Token')
    time.sleep(1)


def Game_Open(fail, froze):
    if fail == 8 or fail > 8:
        fail, froze = Fail(fail=fail, froze=froze)
        fail = 0
    else:
        print(f'Failed/Froze Count: {fail}/{froze}')
    pas = fail
    l = False
    trying = 0
    while l == False:
        print(f'Try Opening {trying}')
        if pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'):
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'))
            time.sleep(30)
            print(f'test{trying} part 1')
            if pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                l = True
            elif pyautogui.locateOnScreen(r'Atlas_img/Loading.png'):
                print('Took To Long')
                Reset_Game()
            elif pyautogui.locateOnScreen(r'Atlas_img/Scheduled_Maintenance.png'):
                Scheduled_Maintenance()
                time.sleep(30)
                l = True
        elif pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png'):
            pyautogui.doubleClick(pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png'))
            time.sleep(5)
            full = False
            while full == False:
                full = pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png')
            pyautogui.click(full)
            time.sleep(2)
            print(f'test{trying} part 2')
            if pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                l = True
            elif pyautogui.locateOnScreen(r'Atlas_img/Loading.png'):
                print('Took To Long')
                fail = Reset_Game(fail=pas)
            elif pyautogui.locateOnScreen(r'Atlas_img/Scheduled_Maintenance.png'):
                Scheduled_Maintenance()
                time.sleep(30)
                l = True
        if trying == 8:
            fail += 1
            print(f"{fail} FAILED")
            return fail, froze
        elif trying != 8:
            trying += 1

    return fail, froze


def Reset_Game():
    print('Restarting Game')
    pyautogui.press(reset_game)
    time.sleep(5)






