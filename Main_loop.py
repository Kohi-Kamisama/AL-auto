import time

from Atlas_Functions import *

fail = 0
froze = 0
time.sleep(4)
pas = 0
print('Starting')
while x == 0:
    boost = 0
    test_fail = True
    while test_fail == False:
        print(f'Checking Fail {fail}')
        if fail > 8:
            print('Grater')
            if froze < 4 or froze != 4:
                froze += 1
                fail = 0
                print('Game Failed')
            elif froze > 4:
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
                elif Game_Shortcut():
                    print('Launching Game')
                    pyautogui.doubleClick(Game_Shortcut())
                    time.sleep(5)
                    if pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png'):
                        pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png'))
                        print('Game Launched')
                    froze = 0
                    fail = 0
        elif fail < 8:
            print(f'Failed/Froze Count: {fail}/{froze}')
            test_fail = True
    game_open = False
    opening = 0

    while game_open == False:
        if opening == 4 or opening > 4:
            Reset_Game()
            fail += 1
            time.sleep(1)
            opening = 0
        else:
            opening += 1

        print(f'Opening {opening}/4')

        if pyautogui.locateOnScreen(r'Atlas_img/Login.png'):
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Login.png'))
            time.sleep(10)

        if pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'):
            print('Found App')
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Game_App.png'))
            time.sleep(5)

        elif Game_Shortcut():
            pyautogui.doubleClick(Game_Shortcut())
            print('Found Shortcut')
            time.sleep(2)
            full = False
            while full == False:
                full = pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png')
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Blue_Square.png'))
            time.sleep(20)

        elif pyautogui.locateOnScreen(r'Atlas_img/Map.png'):
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Map.png'))
            time.sleep(2)
            if pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                game_open = True
                print('Opened')
            else:
                Reset_Game()

        elif pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
            game_open = True
            print('Opened')

        elif pyautogui.locateOnScreen(r'Atlas_img/Scheduled_Maintenance.png'):
            Scheduled_Maintenance()

        elif pyautogui.locateOnScreen(r'Atlas_img/Loading.png'):
            time.sleep(20)
            if pyautogui.locateOnScreen(r'Atlas_img/Loading.png'):
                Reset_Game()

        elif pyautogui.locateOnScreen(r'Atlas_img/Connection_Failed.png'):
            Reset_Game()



    while boost != 4:

        if pyautogui.locateOnScreen(r'Atlas_img/Boost.png'):
            print('Boost Found')
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Boost.png'))
            time.sleep(1)
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Watch_Ad.png'))
            time.sleep(1)
            if pyautogui.locateOnScreen(r'Atlas_img/Unavailable_Ad.png'):
                Reset_Game()
#            elif pyautogui.locateOnScreen(r'Atlas_img/Ad_Not_Ready.png'):
#                Reset_Game()
#            elif pyautogui.locateOnScreen(r'Atlas_img/Max_Boost.png'):
#                pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Max_Boost.png'))
            else:
                Closing_Ad()
        elif not pyautogui.locateOnScreen(r'Atlas_img/Boost.png'):
            boost += 1
            print(f'Looking For Boost {boost}/4')

    if pyautogui.locateOnScreen(r'Atlas_img/Hunt.png'):
        print('Going Hunting')
        pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Hunt.png'))
        time.sleep(5)

        if not pyautogui.locateOnScreen(r'Atlas_img/Green_Hunt.png'):
            Reset_Game()

        elif not pyautogui.locateOnScreen(r'Atlas_img/Next_Spin.png'):
            print('Hunting')
            time.sleep(2)
            hunt = False
            if pyautogui.locateOnScreen(r'Atlas_img/Spin_Wheel.png'):
                spin = pyautogui.locateOnScreen(r'Atlas_img/Spin_Wheel.png')
                pyautogui.click(spin)
                hunt = True
            elif pyautogui.locateOnScreen(r'Atlas_img/Ad_Spin.png'):
                spin = pyautogui.locateOnScreen(r'Atlas_img/Ad_Spin.png')
                pyautogui.click(spin)
                hunt = True

            hunt_count = 0
            while hunt == True:
                time.sleep(2)
                while pyautogui.locateOnScreen(r'Atlas_img/Spin.png'):
                    print('test')
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Spin.png'))
                    wait = False
                    pyautogui.moveTo(8, 8)
                    time.sleep(1)
                    print('looking')
                    while wait == False:
                        wait = pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png')
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'))
                    print('next')
                    fail -= 1
                    pyautogui.moveTo(8, 8)
                    time.sleep(2)
                while pyautogui.locateOnScreen(r'Atlas_img/Spin_Ad.png'):
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Spin_Ad.png'))
                    Closing_Ad()
                    wait = False
                    time.sleep(2)
                    pyautogui.moveTo(8, 8)
                    while wait == False:
                        wait = pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png')
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'))
                    fail -= 1
                    pyautogui.moveTo(8, 8)
                    time.sleep(2)
                if pyautogui.locateOnScreen(r'Atlas_img/Next_Spin.png'):
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Close_Spin.png'))
                    hunt = False
                else:
                    if hunt_count >= 5:
                        hunt = False
                    elif hunt_count < 5:
                        hunt = True
                        hunt_count += 1

        elif pyautogui.locateOnScreen(r'Atlas_img/Next_Spin.png'):
            print('Going Shopping')
            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Shop.png'))
            pyautogui.moveTo(8, 8)

            if pyautogui.locateOnScreen(r'Atlas_img/Green_Shop.png'):
                pyautogui.moveTo(2850, 1169)
                time.sleep(1)
                pyautogui.drag(0, -300, 1, button='left')

            time.sleep(1)
            free = False
            sec = 0
            while free == False:
                if pyautogui.locateOnScreen(r'Atlas_img/Free.png'):
                    print('Watching Video')
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Free.png'))
                    time.sleep(5)
                    if pyautogui.locateOnScreen(r'Atlas_img/Unavailable_Ad.png'):
                        Reset_Game()
                        free = True
                    else:
                        Closing_Ad()
                        time.sleep(1)
                        if pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'):
                            print('CONGRATS!!!')
                            pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Free_Continue.png'))
                            free = True
                            fail -= 1
#                elif pyautogui.locateOnScreen(r'Atlas_img/Shop_Error.png'):
#                    Reset_Game(fail= fail)
#                    free = True
                elif pyautogui.locateOnScreen(r'Atlas_img/Shop.png'):
                    Reset_Game()
                    free = True
                if sec == 600:
                    print('Going Back')
                    map = False
                    while map == False:
                        map = pyautogui.locateOnScreen(r'Atlas_img/Map.png')
                    pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Map.png'))
                    if pyautogui.locateOnScreen(r'Atlas_img/Green_Map.png'):
                        fail -= 1
                    free = True
                elif sec != 600:
                    sec += 1
        else:
            print('Nothing Happened')
            if pyautogui.locateOnScreen(r'Atlas_img/Map.png'):
                pyautogui.click(pyautogui.locateOnScreen(r'Atlas_img/Map.png'))

            else:
                Reset_Game()
    pas += 1
    print(pas)
    fail += 1