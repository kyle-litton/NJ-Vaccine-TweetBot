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

url = "https://mcapps.co.monmouth.nj.us/web/healthdept/vaccine.aspx"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')

Tweet_Timer = 0

print("Searching for appointments...")
while True:
    #print('\n')

    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(2.4,3.3))
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue


    # Check the default message, if it is different then portal is open
    try:
        msg = driver.find_element_by_xpath('//*[@id="Panel2"]/p')
        if 'at this time all appointments have been taken.' not in msg.text:
            driver.get_screenshot_as_file("Screenshots/Monmouthcapture.png")

            status = 'Monmouth county residents only: Monmouth County portal open at this link, https://mcapps.co.monmouth.nj.us/web/healthdept/vaccine.aspx'
            imagePath = "Screenshots/Monmouthcapture.png"
            if time.time() - Tweet_Timer > 150 or Tweet_Timer == 0:

                print("Appointment found.")
                #api.update_with_media(imagePath, status)
                Tweet_Timer = time.time()
                playsound('Beep.m4a')
 

    except:
        #print("Message not found")
        continue