import os
#importing things
import PIL
import pyautogui
from time import sleep
import win32api, win32con

#getting the scroll speed
#scroll=int(input("Enter scroll speed. default is 490. higher is faster. \nLeave blank for default.\nspeed: "))
# if not scroll:
#     scroll=-490
# elif scroll>0:
#     scroll*=-1
delay=3.0

def click(position):
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

scroll=-490
confidence=1
failStreak=0

while pyautogui.position()[0]>5 and pyautogui.position()[1]>-1075:
    try:
        button_location = pyautogui.locateOnScreen('button.png', confidence=confidence, grayscale=False)
        print(f"Found button with confidence {confidence}")
        break
    except Exception as e:
        confidence-=.025
        print(confidence, e)
button_location=None

while pyautogui.position()[0]>5 and pyautogui.position()[1]>-1075:
    try:
        button_location = pyautogui.locateOnScreen('button.png', confidence=confidence, grayscale=False)
        button_x, button_y=pyautogui.center(button_location)
        position=button_x, button_y
        click(position)
        failStreak=0
        print("clicked button")
    except:
        failStreak+=1
        print("fail streak = " + str(failStreak))
        if failStreak==5:
            confidence-=.025
            print(confidence)
            failStreak=0
    button_location = None

    #scroll
    pyautogui.scroll(scroll)
    print("scrolled\n")
    sleep(delay)
print("quitting")
sleep(1)
quit()
