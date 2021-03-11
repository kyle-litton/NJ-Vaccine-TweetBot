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

url = "https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')
while True:

    driver.get(url)
    time.sleep(2)
    mainFrame = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]'))
    )
    
    try:
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="D6F73C26-7627-4948-95EA-2C630C25C5E9_scheduleOpenings_OpeningsData"]'))
    )
    except:
        continue
    
    if element.get_attribute("class") == 'openingsData':
        playsound('Beep.m4a')
        driver.get_screenshot_as_file("Screenshots/HMHNcapture.png")

        status = "Hackensack Meridian: Portal is open at this link https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"
        imagePath = "Screenshots/HMHNcapture.png"

        api.update_with_media(imagePath, status)
        break



#frame = driver.find_element_by_xpath('/html/body/div/div/div[2]/main/div[3]/div/div/iframe')
#driver.switch_to.frame(frame)

#element = driver.find_element_by_xpath('//*[@id="no-times-available-message"]')

#driver.execute_script("arguments[0].scrollIntoView();", element)
#driver.get_screenshot_as_file("capture.png")