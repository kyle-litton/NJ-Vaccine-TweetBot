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

key_file = 'keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

url = "https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')


while True:

    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(1.4,2.3))
    except:
        time.sleep(random.uniform(120,150))
        print("URL Did not load.")
        continue



    # TODO may not need to do this: Check if the curo-root tag is there, avoids the white loading screen
    try:
        root = WebDriverWait(driver, random.uniform(1.7,2.2)).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root'))
        )
    except:
        time.sleep(random.uniform(3.2,4.6))
        print("No root tag.")
        continue

    

    try: # Look for Step 1/13 Introduction page, if not found, continue refreshing
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps'))
        )

        playsound('Beep.m4a')
        driver.get_screenshot_as_file("Screenshots/VNACJcapture.png")

        status = "VNACJ: Portal is open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"
        imagePath = "Screenshots/VNACJcapture.png"

        print(element.get_attribute("class"))

        # TODO uncomment once we have it fully working
        # api.update_with_media(imagePath, status)
        break
        
    except: # Portal not open, no appointmetns
        print("portnal not open")
        continue


    #TODO try: # Portal is open, click the continue button on the introduction page

        # TODO click continue button here
    
    #except: # Could not click continue button
        #continue
















