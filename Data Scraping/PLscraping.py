from difflib import Match
from lib2to3.pgen2 import driver
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd
import numpy as np
import urllib.request
import ast


bookList=[]

def launchWebpage(url):
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
        
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=options)
    driver.set_window_size(1120, 1000)

    driver.get(url)

    return driver

def scrollDown(driver):
    # Scroll down
    current_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 	# Scroll step
        time.sleep(5) 	# Wait to load page
        try:
            new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height
        except:
            print("Failed: ", new_height)
        if new_height == current_height: # Compare with last scroll height
            break
        current_height = new_height

    print("scorlled till",current_height)

def getBooks(driver):

    BooksLinks=[]
    numberOfBooks= 68730
    for i in range(68650,numberOfBooks ):
        link = "https://www.gutenberg.org/ebooks/{}".format(i)
        BooksLinks.append(link)

    for i, link in enumerate(BooksLinks, start=68650):
        driver.get(link)
        
        timeout = 10
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cover']/img")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            continue

        try:
            img= driver.find_elements(By.XPATH, "//*[@id='cover']/img")
            for coverSrc in img:
                src = coverSrc.get_attribute('src')
                        
            coverName= "D:/books4/{}.jpg".format(i)
            urllib.request.urlretrieve(src, coverName)

        except NoSuchElementException:
            print("No more books")
    

if __name__ == "__main__":
   
    link = "https://www.gutenberg.org/ebooks"
    driver= launchWebpage(link)
    getBooks(driver)

    driver.quit()