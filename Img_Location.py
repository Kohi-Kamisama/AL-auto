import pyautogui


def Game_Shortcut():
    game_shortcut = False
    while game_shortcut == False:
        game_shortcut = pyautogui.locateOnScreen(r'Atlas_img/Game_Shortcut.png', confidence=.6)
    return game_shortcut


reset_game = 'r'
