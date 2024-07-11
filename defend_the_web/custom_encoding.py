# Decodes the content of the clipboard when pressing 'c' and copies the result back into the clipboard

from pynput import keyboard
from tkinter import Tk

VISIBLE_CHARACTERS = 94


def on_press(key):
    try:
        if key.char == 'c':
            clipboard_text: str = Tk().clipboard_get()
            values: list[str] = clipboard_text.split(',')
            for i in range(len(values)):
                if values[i] == ' ':
                    continue
                original_ascii = VISIBLE_CHARACTERS - (int(values[i]) - 32) + 32
                values[i] = chr(original_ascii)
            Tk().clipboard_clear()
            Tk().clipboard_append(''.join(values))
        return
    except AttributeError:
        return


def on_release(key):
    if key == keyboard.Key.esc:
        exit(0)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
