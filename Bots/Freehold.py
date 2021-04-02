from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

url = 'https://outlook.office365.com/owa/calendar/MonmouthCountyCOVID19Vaccination@mcsonj.org/bookings/?fbclid=IwAR1gEO6Qrr7GKlf64fNFHu2F9q_Vbdmorm_2IMcigkLIsLfWM-QeM7mfD0o'

chrome_options = Options()
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
    except:
        time.sleep(random.uniform(120,150))
        print("URL Did not load.")
        continue

    try:
        radio_btn = driver.find_element_by_xpath('//*[@id="mainContainer"]/div/form/div[5]/div/ul/li[1]')
        radio_btn.click()
        time.sleep(random.uniform(1.4,2.3))

        numApts = 0
        while True:
            change_month = driver.find_element_by_xpath('//*[@id="mainContainer"]/div/form/div[6]/div[1]/div/div/div[1]/div[2]')

            calendar = driver.find_element_by_xpath('//*[@id="mainContainer"]/div/form/div[6]/div[1]/div/div/div[3]')
            dates = calendar.find_elements_by_tag_name('div')
            for x in dates:
                if x.get_attribute("class") != 'date empty' and x.get_attribute("class") != 'date circle not-bookable':
                    numApts += 1
                    driver.get_screenshot_as_file("../Screenshots/FreeholdCapture.png")
                    print('Appt found')
                    print(x.get_attribute("class"))
                    while True:
                        time.sleep(100000)


            if change_month.get_attribute("class") == 'navigator focusable disabled':
                break
            change_month.click()
        '''
        if numApts > 0:
            driver.get_screenshot_as_file("../Screenshots/FreeholdCapture.png")
            status = 'Monmouth County (Freehold):  {0} appointment(s) open at this link https://outlook.office365.com/owa/calendar/MonmouthCountyCOVID19Vaccination@mcsonj.org/bookings/?fbclid=IwAR1gEO6Qrr7GKlf64fNFHu2F9q_Vbdmorm_2IMcigkLIsLfWM-QeM7mfD0o\n\n Double check eligibility first.'.format(numApts)
            imagePath = "../Screenshots/FreeholdCapture.png"

            if time.time() - Tweet_Timer > 270 or Tweet_Timer == 0:
                api.update_with_media(imagePath, status)
                print('{0} Appointment(s) found.'.format(numApts))
                Tweet_Timer = time.time()
        '''

    except:
        continue
        