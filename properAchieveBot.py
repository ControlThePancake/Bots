from os import close 
import selenium
from selenium import webdriver
from multiprocessing import Process
import functools as ft
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import undetected_chromedriver as uc


numOfBots = 2

questions = {'When light refracts it always changes:':"button_4",
            'The diagram below represents light passing from one medium to another.':"button_3",
            'The following diagram represents the refraction of light as it passes from air into glass':"button_4",
            'The following diagram represents the refraction of red light as it passes from one substance into another:':"button_4",
            'A group of students make the following statements about light refracting when it enters a more dense substance:':"button_4",
            'A group of students make the following statements about light refracting when it enters a less dense substance:':"button_1",
            'A ray of red light with a wavelength 630 nm (6.3 × 10-7 m) passes into a block of glass. The frequency of the wave stays the same and the speed of the light decreases to 2 × 108 ms-1 inside the glass. Calculate the new wavelength of the light inside the glass.':"button_1"}


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
time.sleep(1)

def initiailise():
    driver.get("https://achieve.hashtag-learning.co.uk/user-start/?next=/assess/assess-home/")
    continue_link = driver.find_element(By.LINK_TEXT, 'Sign In')
    continue_link.click()
    time.sleep(1)
    login = driver.find_element(By.NAME, "login")
    thing = input("enter your email for login")
    login.send_keys(thing)
    time.sleep(1)
    password = driver.find_element(By.NAME, "password")
    passw = input("Enter your password")
    password.send_keys(passw)
    time.sleep(1)
    submitButton = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div[2]/div/div/div[2]/form/button")
    submitButton.click()
    time.sleep(2)
    course_name = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/main/div/div[1]/div/div[2]/div[1]/div[9]/form/button/i")
    course_name.click()
    time.sleep(2)
    assess = driver.find_element(By.LINK_TEXT, 'Assess')
    assess.click()
    time.sleep(2)
    start()
    
    
def start():
    assessCourse = driver.find_element(By.PARTIAL_LINK_TEXT, 'Assess Topic')
    assessCourse.click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[2]/main/div/div[6]/div/div[2]/div[8]/div/a")))
    topic = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/main/div/div[6]/div/div[2]/div[8]/div/a")
    topic.click()
    question()

def question():
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[2]/main/div/form/div/div/div[2]/div/div[6]/div/form")))
    questionNum = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/main/div/form/div/div/div[2]/div/div[6]/div/form")
    questionNum.click()
    for i in range(6):
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[2]/main/div/div[2]/div[1]/div/div/p[1]")))
        question_element = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/main/div/div[2]/div[1]/div/div/p[1]")
        question_text = question_element.text
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,questions[question_text])))
        question_answer = driver.find_element(By.ID,questions[question_text])
        question_answer.click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "next")))
        next_button = driver.find_element(By.ID, "next")
        next_button.click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[2]/main/div/div[2]/div[1]/div/div/p[1]")))
    question_element = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/main/div/div[2]/div[1]/div/div/p[1]")
    question_text = question_element.text
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,questions[question_text])))
    question_answer = driver.find_element(By.ID,questions[question_text])
    question_answer.click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,"//*[@id='finish']")))
    finish = driver.find_element(By.XPATH,"//*[@id='finish']")
    finish.click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT,"Done")))
    done = driver.find_element(By.LINK_TEXT,"Done")
    done.click()
    driver.get("https://achieve.hashtag-learning.co.uk/assess/544/topic/choose-questions/")
    print(f"Success")
    question()

#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "btn btn-assess-choice btn-block")))

def runInParallel(count):
    proc = []
    for i in range(0, count):
        p = Process(target=initiailise)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

if __name__ == '__main__':
    runInParallel(numOfBots)
