"""
Author: Igor Assuncao
Desc: Script to simulate numpad Hotkeys using their Virtual Key Codes
"""

from pynput import keyboard
from pynput.keyboard import Key, Controller

"""
#   Key          Virtual Key Code
# 1			49
# 2			50
# 3			51
# 4			52
# 5			53
# 6			54
# 7			55
# 8			56
# 9			57
# 0			48
# Numpad 1		97
# Numpad 2		98
# Numpad 3		99
# Numpad 4		100
# Numpad 5		101
# Numpad 6		102
# Numpad 7		103
# Numpad 8		104
"""

keyboardController = Controller()

def on_press(key):
    if key == keyboard.KeyCode(49):
        keyboardController.press(keyboard.KeyCode(103))
    elif key == keyboard.KeyCode(50):
        keyboardController.press(keyboard.KeyCode(104))
    elif key == keyboard.KeyCode(51):
        keyboardController.press(keyboard.KeyCode(100))
    elif key == keyboard.KeyCode(52):
        keyboardController.press(keyboard.KeyCode(101))
    elif key == keyboard.KeyCode(53):
        keyboardController.press(keyboard.KeyCode(97))
    elif key == keyboard.KeyCode(54):
        keyboardController.press(keyboard.KeyCode(98))
    else:
        pass

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()

