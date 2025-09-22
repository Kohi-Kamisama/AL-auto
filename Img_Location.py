import pyautogui
import pyscreeze


def Game_Shortcut():
    game_shortcut = False
    while game_shortcut == False:
        print(game_shortcut)
        # game_shortcut = pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png', confidence=.6)
        try:
            return pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png', confidence=.6)
        except pyautogui.ImageNotFoundException:
            return False
    return game_shortcut


def Locate(img):
    try:
        return pyautogui.locateOnScreen(img)
    except pyautogui.ImageNotFoundException:
        return None


reset_game = 'r'
