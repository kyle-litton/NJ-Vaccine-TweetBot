from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from selenium.webdriver.support.color import Color
import tweepy
import random
import time
import json

def countAppointments(availability_container):
    # TODO get the correct green color vvvvvvv and update this placeholder

    GREY_COLOR = Color.from_string('#F4F6F7')
    total = 0
    col = 1
    row = 2

    all_cols = availability_container.find_elements_by_xpath(".//*")

    # TODO this is hard coded, maybe try to find a better way
    num_cols  = 7

    #vvvv all time slots + headers all_cols/2 - number of headers
    num_rows = (int(len(all_cols))/2 - num_cols) / num_cols
    
    while col <= num_cols:
        while row <= num_rows:
            try: # Check the background color of each appt, if green add to total
                cur_time_slot = availability_container.find_element_by_xpath('.//div[{0}]/div[{1}]/div'.format(col, row))
                button_color = Color.from_string(cur_time_slot.value_of_css_property('background-color'))
              
                if button_color != GREY_COLOR:
                    total+=1
            except:
                row+=1
                continue
            row+=1
        row = 2
        col+=1
 
    return total



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
        #print("URL Did not load.")
        continue



    # TODO may not need to do this: Check if the curo-root tag is there, avoids the white loading screen
    try:
        root = WebDriverWait(driver, random.uniform(1.7,2.2)).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root'))
        )

    except:
        time.sleep(random.uniform(3.2,4.6))
        #print("No root tag.")
        continue

    

    try: # Look for Step 1/13 Introduction page, if not found, continue refreshing
        registration_page = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/button'))
        )
        
    except: # Portal not open, no appointmetns
        #print("portal not open")
        continue


    try: # Portal is open, click the Get Started button on the introduction page
        #print("trying to click button")
        get_started_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/button'))
        )
        get_started_button.click()

    
    except: # Could not click continue button
        #print("couldnt click button")
        continue


    try: # Click first location
        #print("trying to click location")
        
        loc_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-locations/div/div[2]/div[3]/div[1]/div[1]'))
        ).text
        #print(loc_1)
        
        location_1_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-locations/div/div[2]/div[3]'))
        )
        location_1_button.click()
        time.sleep(random.uniform(1.4,2.3))

    
    except: # Could not click continue button
        #print("couldnt click location")
        continue


    try: # Count appointments for first location
        #print("click button worked")
        openAppts = 0
        loc1_availability_container = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]'))
        )
        openAppts += countAppointments(loc1_availability_container)
        #print("line 128")
        if openAppts > 0:
            print("i found")
            print(openAppts)
            print("open appts at:")
            print(loc_1)
            
            
            driver.get_screenshot_as_file("Screenshots/VNACJcapture.png")

            status = "VNACJ: Portal is open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"
            imagePath = "Screenshots/VNACJcapture.png"

            playsound('Beep.m4a')
            print("after beep")
            # TODO uncomment once we have it fully working
            # api.update_with_media(imagePath, status)
            break
        
    except:
        continue



    # TODO count appointments for the other 2 locations too