"""
Author: Igor Assuncao
Desc: Script to simulate Hotkeys using their Virtual Key Codes,
        in this case I'm simulating some numpad keys.
"""

from pynput import keyboard
from pynput.keyboard import Key, Controller

"""
Check this link for the virtual key codes:
    https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
Please, keep in mind that their using their 0x<HexValues>, for example
Numpad 0 = 0x60, so you have to convert the HexValue to Decimal in order to use properly.
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

