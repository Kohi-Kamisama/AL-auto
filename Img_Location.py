import pyautogui
import pyscreeze


def Game_Shortcut():
    game_shortcut = False
    while game_shortcut == False:
        game_shortcut = pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png', confidence=.6)
    return game_shortcut


def Locate(img):
    try:
        return pyautogui.locateOnScreen(img)
    except pyscreeze.ImageNotFoundException:
        return none


reset_game = 'r'
