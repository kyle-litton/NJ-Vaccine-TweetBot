from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
import tweepy
import time
import json

key_file = 'keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

url = "https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1/blocked"

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')
while True:

    driver.get(url)
    time.sleep(2)
    mainFrame = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-blocked'))
    )
    
    # TODO fix this try/except to be the correct way once we see open VNACJ appts

    try: # Look for error page, if found continue refreshing
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-blocked/section/h1'))
    )
        continue

    except: # Error page didn't load --> there may be appointments

        playsound('Beep.m4a')
        driver.get_screenshot_as_file("Screenshots/VNACJcapture.png")

        status = "VNACJ: Portal is open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1/blocked"
        imagePath = "Screenshots/VNACJcapture.png"

        print(element.get_attribute("class"))

        # TODO uncomment once we have it fully working
        # api.update_with_media(imagePath, status)
        break

