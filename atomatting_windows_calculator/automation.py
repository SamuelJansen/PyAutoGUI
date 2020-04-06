import pyautogui, time

# time.sleep(5)
# pyautogui.click()
#
# distance = 400
#
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration = 0.2)
#     distance -= 50
#     pyautogui.dragRel(0, distance, duration = 0.2)
#     distance -= 50
#     pyautogui.dragRel(-distance, 0, duration = 0.2)
#     distance -= 50
#     pyautogui.dragRel(0, -distance, duration = 0.2)
#     distance -= 50

pyautogui.FAILSAFE = True

print(pyautogui.locateCenterOnScreen('one.png'))
one_position = pyautogui.locateCenterOnScreen('one.png')
print(one_position)
pyautogui.click(one_position)
pyautogui.click(one_position)

print(pyautogui.locateCenterOnScreen('plus.png'))
plus_position = pyautogui.locateCenterOnScreen('plus.png')
print(plus_position)
pyautogui.click(plus_position)
pyautogui.click(plus_position)

print(pyautogui.locateCenterOnScreen('five.png'))
five_position = pyautogui.locateCenterOnScreen('five.png')
print(five_position)
pyautogui.click(five_position)
pyautogui.click(five_position)

print(pyautogui.locateCenterOnScreen('equals.png'))
equals_position = pyautogui.locateCenterOnScreen('equals.png')
print(equals_position)
pyautogui.click(equals_position)
pyautogui.click(equals_position)
