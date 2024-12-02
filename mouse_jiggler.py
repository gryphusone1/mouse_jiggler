import pyautogui
import time

def jiggle_mouse():
    while True:
        pyautogui.move(1, 1, duration=0.1)
        pyautogui.move(-1, -1, duration=0.1)
        time.sleep(5)

if __name__ == "__main__":
    jiggle_mouse()