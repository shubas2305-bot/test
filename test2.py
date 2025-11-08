import pyautogui
import time
import webbrowser
# Step 1: Open Google
webbrowser.open("https://www.google.com")
time.sleep(1)
pyautogui.click(450,292)
time.sleep(1)
pyautogui.write("make my trip")
pyautogui.press("enter")
time.sleep(1)
pyautogui.middleClick(268,383)
pyautogui.press("enter")
time.sleep(1)


