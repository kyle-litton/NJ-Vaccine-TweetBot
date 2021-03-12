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

HMHN_Timer = 0

print("Searching for appointments...")
while True:

    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(3)

    # Check if the main tag is there, avoids the high traffic page and makes the other tags readable
    try:
        mainFrame = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]'))
        )
    except:
        time.sleep(5)
        continue
    
    # Find the OpeningsData div, used to check whether any open appointments
    try:
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="D6F73C26-7627-4948-95EA-2C630C25C5E9_scheduleOpenings_OpeningsData"]'))
    )
    except:
        continue

    try:
        # This element is used to prevent case of loading heart in screenshot
        heart = driver.find_element_by_xpath('/html/body/div[12]')

            # Final check to make sure there are appointments and no loading heart
        try:
            slotList = driver.find_element_by_xpath('//*[@id="D6F73C26-7627-4948-95EA-2C630C25C5E9_scheduleOpenings_OpeningsData"]/div/div/div[4]/div/div[3]')
            if slotList.get_attribute("class") == 'slotslist hasScrollIndicator' and heart.get_attribute("class") == 'ajaxspinner defaultajaxoverlay hidden':
                playsound('Beep.m4a')
                driver.get_screenshot_as_file("Screenshots/HMHNcapture.png")

                status = "Hackensack Meridian: Portal is open at this link https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"
                imagePath = "Screenshots/HMHNcapture.png"

                # Only tweet again after 8 min
                print("Appointment found.")
                api.update_with_media(imagePath, status)
                HMHN_Timer = time.time()

                break
        except:
            continue

    except:
        continue


# TODO use this for rowan website
#frame = driver.find_element_by_xpath('/html/body/div/div/div[2]/main/div[3]/div/div/iframe')
#driver.switch_to.frame(frame)

#element = driver.find_element_by_xpath('//*[@id="no-times-available-message"]')

#driver.execute_script("arguments[0].scrollIntoView();", element)
#driver.get_screenshot_as_file("capture.png")