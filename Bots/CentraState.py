from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
import tweepy
import random
import time
import json

key_file = '../keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

url = "https://centrastatevac.wpengine.com/vaccine-appointment-request/?twid=njv"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1200,824")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options,executable_path='../Drivers/chromedriver')

print("Searching for registration form...")
while True:
    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(2.9,4.3))
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue

    
    try: # Check the header message
        header_message = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[4]/div/div/div/h1'))
        )

        if header_message.text == 'PROTECTED: VACCINE APPOINTMENT REQUEST':
            #print("no appts")
            continue

        else: # Portal is open
            print("portal open")
            reg_form = driver.find_element_by_xpath('//*[@id="post-69719"]/div/div[2]')
            driver.execute_script("arguments[0].scrollIntoView()", reg_form)
            driver.get_screenshot_as_file("../Screenshots/CentraStateCapture.png")
            
            status = "CentraState (Freehold) Form is open at this link https://centrastatevac.wpengine.com/vaccine-appointment-request/?twid=njv \n\nPay attention to age requirements\nAfter submitting this registration, you should receive a call within a few days to schedule your appointment."
            imagePath = "../Screenshots/CentraStateCapture.png"

            # TODO uncomment once we have it fully working
            api.update_with_media(imagePath, status)
            break
            
        
    except: # Error loading header on page
        time.sleep(random.uniform(110,140))
        #print("Header Did not load.")
        continue
        