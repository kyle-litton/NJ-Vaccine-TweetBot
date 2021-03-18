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
        registration_page = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps'))
        )
        
    except: # Portal not open, no appointmetns
        print("portal not open")
        continue


    try: # Portal is open, click the Get Started button on the introduction page

        # TODO click continue button here
        get_started_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/button'))
        )
        get_started_button.click()
    
    except: # Could not click continue button
        continue


    try: # Count appointments for first location
        openAppts = 0
        loc1_availability_container = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]'))
        )
        openAppts += countAppointments(availability_container)

        if openAppts > 0:
            playsound('Beep.m4a')
            driver.get_screenshot_as_file("Screenshots/VNACJcapture.png")

            status = "VNACJ: Portal is open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"
            imagePath = "Screenshots/VNACJcapture.png"

            print(element.get_attribute("class"))

            # TODO uncomment once we have it fully working
            # api.update_with_media(imagePath, status)
            break
        
    except:
        continue



    # TODO count appointments for the other 2 locations too





def countAppointments(availability_container):
    # TODO get the correct green color vvvvvvv and update this placeholder
    GREEN_COLOR = Color.from_string('#2F7ED8')
    total = 0
    col = 1
    row = 2

    num_cols = availability_container.childElementCount

    col1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]/div[1]'))
        )

    num_rows = col1.childElementCount
  

    while col <= num_cols:
        while row <= num_rows:
            try: # Check the background color of each appt, if green add to total
                cur_time_slot = WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]/div[{0}]/div[{1}]/div'.format(num_col, num_row)))
                            )
                button_color = Color.from_string(cur_time_slot.value_of_css_property('background-color'))
  
                if button_color == GREEN_COLOR:
                    total+=1
            except:
                continue
            row+=1
        col+=1

    return total










