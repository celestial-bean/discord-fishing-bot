import os
#importing things
try:
    import PIL
except ImportError:
    os.system("pip install Pillow")
    import PIL
try:
    import pyautogui
except ImportError:
    os.system("pip install pyautogui")
    import pyautogui
try:
    from time import sleep
except ImportError:
    os.system("pip install time")
    from time import sleep
try:
    import win32api, win32con
except ImportError:

    os.system("pip install pywin32")
    import win32api, win32con
os.system("pip install opencv-python")

#getting the scroll speed
#scroll=int(input("Enter scroll speed. default is 490. higher is faster. \nLeave blank for default.\nspeed: "))
# if not scroll:
#     scroll=-490
# elif scroll>0:
#     scroll*=-1
scroll=-490
confidence=0.9
failStreak=0

def click():
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#ignore

##while True:
##    button_location = pyautogui.locateOnScreen('heart.png', confidence=confidence)
##    if button_location==None:
##        confidence-=.025
##    else:
##        break

    #find the heart button and click it
# while True:
#     print(pyautogui.position())
#     sleep(.5)
while pyautogui.position()[0]>5 and pyautogui.position()[1]>-1075:
    button_location = pyautogui.locateOnScreen('button.png', confidence=confidence, grayscale=False)
    if button_location!=None:
        button_x, button_y=pyautogui.center(button_location)
        position=button_x, button_y
        click()
        failStreak=0
        print("clicked button")
    else:
        failStreak+=1
        print("fail streak = " + str(failStreak))
        #confidence-=.05
    button_location = None

    #scroll
    pyautogui.scroll(scroll)
    print("scrolled\n")
    sleep(3.51)
print("quitting")
sleep(1)
quit()
