
from os import close 
import selenium
from selenium import webdriver
from multiprocessing import Process
import functools as ft

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def start():
    game_code = int(input("Enter game code:/n")) 
    bot_num = int(input("Enter the amount of bots:/n"))   
    print(game_code, bot_num)
    runInParallel(bot_num, game_code)

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
    start()
