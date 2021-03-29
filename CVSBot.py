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

url = "https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns"

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--window-size=1200,824")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')



print("Searching for appointments...")
while True:
    try: # Load initial page
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(1.4,2.3))
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue

    try: # Look for zip code search bar
        default_page = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="no-times-available-message"]'))
        )

    except: # Zip code search bar not there -> need to fill out the questionaire
        # First Page of Forms: Click "NO" on all 3 questions
        first_no_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[3]/fieldset/div[2]/div[2]')))
        first_no_button.click()
        time.sleep(random.uniform(3,5.3))
        second_no_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[4]/fieldset/div[2]/div[2]')))
        second_no_button.click()
        time.sleep(random.uniform(6,10.7))
        third_no_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[5]/fieldset/div[2]/div[2]')))
        third_no_button.click()
        time.sleep(random.uniform(1.4,2.3))

        continue_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/button')))
        continue_button.click()
        time.sleep(random.uniform(9,12))

        # Second Page of Forms: Click "I need to start vaccination"
        start_vax = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="generic"]/section/div[2]/div/div/div[1]')))
        start_vax.click()
        time.sleep(random.uniform(3.4,6.3))

        continue_scheduling = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/button')))
        continue_scheduling.click()
        time.sleep(random.uniform(3,5))
        
    
        break
        







#https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns


# //*[@id="content"]/div[2]/cvs-store-locator
# If the zipcode search bar shows up --> don't need to fill out initial form
# If the zipcode search bar does not show up --> DO need to fill out initial form


