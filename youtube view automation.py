from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import tkinter as tk
from PIL import Image, ImageTk

user_input_var = None

def get_string_and_close():
    global user_input_var
    user_input_var = entry.get()
    root.destroy()  

# Create the main Tkinter window
root = tk.Tk()
root.title("Enter Youtube Link")
root.geometry("600x300")

youtube_logo_image = Image.open("C:\\Users\\KIIT\\Downloads\\youtube-icon-512x512-80maysdk.png")  
youtube_logo_image = youtube_logo_image.resize((600, 300), Image.ANTIALIAS)  # Resize the image
youtube_logo = ImageTk.PhotoImage(youtube_logo_image)

bg_label = tk.Label(root, image=youtube_logo)
bg_label.place(relwidth=1, relheight=1)

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# Create a button to submit the input and close the window
submit_button = tk.Button(root, text="Submit", command=get_string_and_close)
submit_button.pack(pady=10)

root.mainloop()

youtube_link = user_input_var

url = "https://plainproxies.com/resources/free-web-proxy"
path = "C:\\Users\\KIIT\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path= path)
driver = webdriver.Chrome(service = service)

for i in range(100):
    
    driver.get(url)
    search_box = driver.find_element(by = "xpath",value= '/html/body/div[1]/section[1]/div/div/div/form/div[2]/input')
    search_box.send_keys(youtube_link)
    time.sleep(1)
    button = driver.find_element(by = "xpath",value= '/html/body/div[1]/section[1]/div/div/div/form/div[2]/div/button')
    button.click()
    time.sleep(15)
    yt_button = driver.find_element(by = "xpath",value= '//*[@id="movie_player"]/div[6]/button')
    yt_button.click()
    time.sleep(40)
    
driver.quit()  
    

    
  
    
    



   
    
    
