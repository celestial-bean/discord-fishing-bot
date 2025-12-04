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
fish_delay=2.7

def click(position):
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

scroll=-490
confidence=1
failStreak=0
delay=fish_delay
while pyautogui.position()[0]>5 and pyautogui.position()[1]>-1075:
    try:
        pyautogui.locateOnScreen('button.png', confidence=confidence, grayscale=False)
        print(f"Found button with confidence {confidence}")
    except:
        try:
            pyautogui.locateOnScreen('button2.png', confidence=confidence, grayscale=False)
            print(f"Found button with confidence {confidence}")
        except:
            try:
                pyautogui.locateOnScreen('back.png', confidence=confidence, grayscale=False)
                print(f"Found button with confidence {confidence}")
            except Exception as e:
                try:
                    pyautogui.locateOnScreen('return.png', confidence=confidence, grayscale=False)
                    print(f"Found button with confidence {confidence}")
                except:
                    try:
                        pyautogui.locateOnScreen('message.png', confidence=confidence, grayscale=False)           
                        print(f"Found button with confidence {confidence}")
                        break
                    except Exception as e:
                        confidence-=.025
                        print(confidence, e)

while pyautogui.position()[0]>5 and pyautogui.position()[1]>-1075:
    try:
        button_location = pyautogui.locateOnScreen('button.png', confidence=confidence, grayscale=False)
        delay=fish_delay
    except:
        try:
            button_location = pyautogui.locateOnScreen('button2.png', confidence=confidence, grayscale=False)
            delay=fish_delay
        except:
            try:
                button_location = pyautogui.locateOnScreen('back.png', confidence=confidence, grayscale=False)
                print("found back button")
                delay=0.5
            except Exception as e:
                try:
                    button_location = pyautogui.locateOnScreen('return.png', confidence=confidence, grayscale=False)
                    print("found return button")
                    delay=0.5
                except:
                    try:
                        print("found message box")
                        button_location = pyautogui.locateOnScreen('message.png', confidence=confidence, grayscale=False)           
                        button_x, button_y=pyautogui.center(button_location)
                        position=button_x, button_y
                        click(position)
                        pyautogui.write("/fish", interval=0.05)
                        pyautogui.press('enter')
                        sleep(0.05)
                        pyautogui.press('enter')
                        delay=fish_delay
                    except:
                        print(e)
                        failStreak+=1
                        print("fail streak = " + str(failStreak))
                        if failStreak==7:
                            confidence-=.0125
                            print(confidence)
                            failStreak=0
                        continue
    button_x, button_y=pyautogui.center(button_location)
    position=button_x, button_y
    click(position)
    failStreak=0
    print("clicked button")
    button_location = None

    #scroll
    pyautogui.scroll(scroll)
    print("scrolled\n")
    sleep(delay)
print("quitting")
sleep(1)
quit()
