import pyautogui as pt
import time

number = int(input("Enter the number of repetitions: "))
message = input("Enter the message: ")

time.sleep(5)

for i in range(0, number):
    pt.write(message)
    pt.press('enter')
