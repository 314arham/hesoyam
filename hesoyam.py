"""
hesoyam.py

Automate the infamous cheat code in GTA: San Andreas "HESOYAM"
By using script bellow, cheat will be performed multiple times. each time it's
entered, in-game money increased by $250 k.

1. run the game
2. press Windows key and get out of game environment
3. run function for sleepTime = 10
4. back to game quickly ( < sleepTime)
5. do not press any key untill the cheat applied n times.

"""
import pyautogui, time
pyautogui.FAILSAFE = True

"""
                        PyAutoGUI
        Cross-platform GUI automation for human beings

Documentation:  https://pyautogui.readthedocs.io/en/latest/
About FAILSAFE: https://automatetheboringstuff.com/chapter18/
"""
def HESOYAM(sleepTime=10, n=10):
 time.sleep(sleepTime)  # wait sleepTime seconds so user could return to game
 cheatCode = 'hesoyam'  # just for simplification
 while n:   # the script supposed to run n times
  for key in cheatCode:
   pyautogui.keyDown(key)   # virtually pressing each key to enter the code
   pyautogui.keyUp(key) # game control will be crashed unless you release keys
  n -= 1
 return 0

"""
# while block could be written like this for better performance:
while n:
 pyautogui.keyDown('h') # h
 pyautogui.keyUp('h')
 pyautogui.keyDown('e') # e
 pyautogui.keyUp('e')
 pyautogui.keyDown('s') # s
 pyautogui.keyUp('s')
 pyautogui.keyDown('o') # o
 pyautogui.keyUp('o')
 pyautogui.keyDown('y') # y
 pyautogui.keyUp('y')
 pyautogui.keyDown('a') # a
 pyautogui.keyUp('a')
 pyautogui.keyDown('m') # m
 pyautogui.keyUp('m')
 n -= 1
"""

HESOYAM(10, 20)
