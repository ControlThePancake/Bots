
from os import close 
import selenium
from selenium import webdriver
from multiprocessing import Process
import tkinter as tk
import functools as ft

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

##My own code(no wonder it dosent work) / tkinter gui bs

def showWindow():
    global window, gc, bn
    ##Ik its a kahoot bot dont judge
    window = tk.Tk()
    window.geometry("300x275")
    window.title("Kahoot Bot v2")

    passwordLabel = tk.Label(window, text = "Enter Game Code").grid(row = 0, column = 0, padx=20, pady=15)
    gc = tk.StringVar()
    gameCode = tk.Entry(window, textvariable=gc).grid(row = 0, column=1)

    botLabel = tk.Label(window, text = "Enter the amount of bots").grid(row = 1, column = 0, padx=10, pady=15)
    bn = tk.StringVar()
    botNum = tk.Entry(window, textvariable=bn).grid(row =1, column=1)
    
    btn_enter = tk.Button(window, text = "Enter",command=start, width = 11, font=("Arial", 14))
    btn_enter.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
    window.mainloop()  

def start():
    game_code = gc.get()
    bot_num = bn.get()   
    window.destroy()
    print(game_code, bot_num)
    runInParallel(int(bot_num), game_code)

def play_game(game_code):
    driver1 = webdriver.Chrome()
    driver1.get("https://www.kahoot.it")
    time.sleep(2)
    pinInput1 = driver1.find_element(By.ID, "game-input")
    time.sleep(2)
    pinInput1.send_keys(game_code)  
    pinInput1.send_keys(Keys.RETURN)
    time.sleep(2)
    nicInput1 = driver1.find_element(By.ID, "nickname")
    nicInput1.send_keys("TotallyLegit" + str(random.randint(0,10000)))
    nicInput1.send_keys(Keys.RETURN)
    while True:
        if len(driver1.find_elements(By.CSS_SELECTOR, "[data-functional-selector=ranking-text]")) > 0:
            break
        WebDriverWait(driver1, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-functional-selector="answer-0"]')))
        answer = random.choice(driver1.find_elements(By.CSS_SELECTOR, "[data-functional-selector^=answer]"))
        answer.click()
        time.sleep(10)
    driver1.quit()

def runInParallel(count, game_code):
    proc = []
    for i in range(0, count):
        p = Process(target=play_game, args=(game_code,))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

if __name__ == '__main__':
    showWindow()
