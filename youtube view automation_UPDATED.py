from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import tkinter as tk
from PIL import Image, ImageTk


url = "https://proxyium.com"
path = "C:\\Coding1\\Coding\\python\\Automation\\chromedriver-win64\\chrome.exe"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\aayus\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\Default")
options.add_argument("profile-directory=Default") 
options.binary_location = path

youtube_link = sys.argv[1]
driver = webdriver.Chrome(options)

for i in range(100):
    
    driver.get(url)
    time.sleep(1)
    search_box = driver.find_element(by="name", value="url") 
    search_box.send_keys(youtube_link)
    time.sleep(1)
    button = driver.find_element(by="css selector", value="button[type='submit']")
    button.click()
    time.sleep(15)
    yt_button = driver.find_element(by = "css selector",value= 'button.ytp-large-play-button')
    yt_button.click()
    time.sleep(40)
    
driver.quit()  
    

    
  
    
    



   
    
    
