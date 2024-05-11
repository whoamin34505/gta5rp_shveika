#Импорт библиотек:
from python_imagesearch.imagesearch import *
import pyautogui 
import time 

#Написание скрипта:
while True:
    button_a = imagesearch("a.jpg") 
    if button_a[0] != -1: 
        print("position: ", button_a[0], button_a[1]) 
        time.sleep(0.1)
        pyautogui.press('a') 
    else: 
        print("A не найдена")
    button_d = imagesearch("d.jpg") 
    if button_d[0] != -1: 
        print("position: ", button_d[0], button_d[1]) 
        time.sleep(0.1)
        pyautogui.press('d') 
    else: 
        print("D не найдена")
    button_s = imagesearch("s.jpg") 
    if button_s[0] != -1: 
        print("position: ", button_s[0], button_s[1]) 
        time.sleep(0.1)
        pyautogui.press('s') 
    else: 
        print("S не найдена")
    button_w = imagesearch("w.jpg") 
    if button_w[0] != -1: 
        print("position: ", button_w[0], button_w[1]) 
        time.sleep(0.1)
        pyautogui.press('w') 
    else: 
        print("W не найдена")
    button_e = imagesearch("e.jpg") 
    if button_e[0] != -1: 
        print("position: ", button_e[0], button_e[1])
        time.sleep(0.1)
        pyautogui.press('e') 
    else: 
        print("E не найдена")


