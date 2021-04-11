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

url = "https://rowanmedicine.com/vaccine/registration.html"

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1200,824")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options,executable_path='../Drivers/chromedriver')

Tweet_Timer = 0

print("Searching for appointments...")
while True:
    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(1.4,2.3))
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(random.uniform(1.4,2.3))
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue

    
    try: # Check the default message, if it is different then portal is open
        default_page = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="no-times-available-message"]'))
        )
        
    except: # Portal is open
        time.sleep(random.uniform(1.2,2.3))

        # Scroll to appt table and screenshot for tweet
        pageBtn = driver.find_element_by_xpath('//*[@id="step-pick-appointment"]/div[3]')   
        driver.execute_script("arguments[0].scrollIntoView()", pageBtn)

        driver.get_screenshot_as_file("../Screenshots/RowanCapture.png")
        numApts = len(driver.find_elements_by_class_name('time-selection'))

        status = 'Rowan Medicine:  {0} appointment(s) open at this link https://rowanmedicine.com/vaccine/registration.html'.format(numApts)
        imagePath = "../Screenshots/RowanCapture.png"

        if (time.time() - Tweet_Timer > 3000 or Tweet_Timer == 0) and numApts > 0:
            api.update_with_media(imagePath, status)
            print('{0} Appointment(s) found.'.format(numApts))
            Tweet_Timer = time.time()

        continue