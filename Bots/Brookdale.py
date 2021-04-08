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

url = "https://www.co.monmouth.nj.us/page.aspx?ID=1932"

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--window-size=1200,824")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options,executable_path='../Drivers/chromedriver')

Tweet_Timer = 0

driver.get(url)
time.sleep(.75)
dismiss_banner = driver.find_element_by_xpath('//*[@id="prefix-dismissButton"]')
dismiss_banner.click()

print("Searching for appointments...")
while True:
    #print('\n')
    try:
        time.sleep(random.uniform(3.4,4.7))
        driver.delete_all_cookies()
        driver.get(url)
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue

    # Check the default message, if it is different then portal is open
    try:
        schedule = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]')
        schedule.click()
        time.sleep(random.uniform(1.3,2.4))


        try:
            msg = driver.find_element_by_xpath('//*[@id="Button1"]')
                     
            driver.get_screenshot_as_file("../Screenshots/Monmouthcapture.png")

            status = 'Monmouth county residents only: Monmouth County portal open at this link, https://www.co.monmouth.nj.us/page.aspx?ID=1932 \n\nClick Schedule a COVID-19 Vaccine and follow the prompts on screen.'
            imagePath = "../Screenshots/Monmouthcapture.png"
            
            print("Portal Open.")
            api.update_with_media(imagePath, status)
            break 
 

        except:
            continue
 

    except:
        #print("Message not found")
        continue