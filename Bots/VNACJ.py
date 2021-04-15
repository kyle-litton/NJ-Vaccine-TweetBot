from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
import tweepy
import random
import time
import json

def countAppointments(availability_container):
    GREY_COLOR = Color.from_string('#F4F6F7')
    total = 0
    col = 1
    row = 2

    # TODO this is hard coded, maybe try to find a better way
    num_cols  = 7
    all_cols = availability_container.find_elements_by_xpath(".//*")
    num_rows = (int(len(all_cols))/2 - num_cols) / num_cols
    
    while col <= num_cols:
        while row <= num_rows:
            try: # Check the background color of each appt, if not grey, add to total
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



key_file = '../keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

url = "https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options,executable_path='../Drivers/chromedriver')

print("Searching for appointments...")
while True:

    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(1.4,2.3))
        root = WebDriverWait(driver, random.uniform(1.7,2.2)).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root'))
        )
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue
    

    try: # Select English on the language page (Step 1/14)
        language_page = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-languages/div/div[2]/div[1]'))
        )
        language_page.click()

        
    except: # Portal not open, no appointmetns
        #print("portal not open")
        continue


    try: # Look for Step 1/13 Introduction page then click get started button, if not found, continue refreshing
        get_started_button = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/button')
        get_started_button.click()
        
    except: # Portal not open, no appointmetns
        #print("portal not open")
        continue


    # Case 1: Location menu shows up, more than one location is open
    try:
        loc1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-locations/div/div[2]/div[3]/div[1]/div[1]'))
        )
        loc1_name = loc1.text
        location_1_button =  driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-locations/div/div[2]/div[3]')
        location_1_button.click()
        time.sleep(random.uniform(1.4,2.3))
     
        screenshot_taken = False
        loc1_openAppts = 0
        loc1_availability_container = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]')
        loc1_openAppts += countAppointments(loc1_availability_container)
        
        if loc1_openAppts > 0:
            driver.get_screenshot_as_file("../Screenshots/VNACJcapture.png")
            screenshot_taken = True

    # Case 2: No menu shows up because only one location is available, page skips to availability page
    except:
        loc1_name = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[1]/curo-appointment-info/div[1]/div[2]').text
        loc1_openAppts = 0

        loc1_availability_container = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]'))
        )
        loc1_openAppts += countAppointments(loc1_availability_container)
        appts_tweet = ''
        # Found appts at the only open location --> screenshot and tween
        if loc1_openAppts > 0:
            driver.get_screenshot_as_file("../Screenshots/VNACJcapture.png")
            screenshot_taken = True
            appts_tweet = appts_tweet + ('\n{0}: {1}'.format(loc1_name,loc1_openAppts))
            intro = "VNACJ: {0} appointments open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1 \n".format(loc1_openAppts)
            status = intro + appts_tweet
            imagePath = "../Screenshots/VNACJcapture.png"
            api.update_with_media(imagePath, status)
            print("Appointment(s) found")
            break

        else: 
            continue


    try: # 2ND LOCATION: Count appointments
        loc2_openAppts = 0

        dropdown_menu = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/ng-select')
        dropdown_menu.click()

        loc2_dropdown = dropdown_menu.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]')
        loc2_dropdown.click()
        time.sleep(random.uniform(0.3,0.7))
        
        loc2 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[1]/curo-appointment-info/div[1]/div[2]'))
        )
        loc2_name = loc2.text

        loc2_availability_container = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]')
        loc2_openAppts += countAppointments(loc2_availability_container)

        if loc2_openAppts > 0 and screenshot_taken == False:
            driver.get_screenshot_as_file("../Screenshots/VNACJcapture.png")
            screenshot_taken = True

    except:
        continue


    try: # 3RD LOCATION: Count appointments
        loc3_openAppts = 0

        dropdown_menu = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/ng-select')
        dropdown_menu.click()

        loc3_dropdown = dropdown_menu.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]')
        loc3_dropdown.click()
        time.sleep(random.uniform(0.3,0.7))

        loc3 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[1]/curo-appointment-info/div[1]/div[2]'))
        )
        loc3_name = loc3.text
        
        loc3_availability_container = driver.find_element_by_xpath('/html/body/curo-root/curo-intel-widget-layout/div/curo-registrations/curo-registration-steps/div/div/div/div[2]/curo-patient-registration/curo-availabilities/section/div[2]')
        loc3_openAppts += countAppointments(loc3_availability_container)

        if loc3_openAppts > 0 and screenshot_taken == False:
            driver.get_screenshot_as_file("../Screenshots/VNACJcapture.png")
            screenshot_taken = True
 
    except:
        continue


    try:
        if screenshot_taken:
            appts_tweet = ''
            total_appts = loc1_openAppts + loc2_openAppts + loc3_openAppts
            
            if loc1_openAppts > 0:
                appts_tweet = appts_tweet + ('\n{0}: {1}'.format(loc1_name,loc1_openAppts))
            if loc2_openAppts > 0:
                appts_tweet = appts_tweet + ('\n{0}: {1}'.format(loc2_name,loc2_openAppts))
            if loc3_openAppts > 0:
                appts_tweet = appts_tweet + ('\n{0}: {1}'.format(loc3_name,loc3_openAppts))

            intro = "VNACJ: {0} appointments open at this link https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1 \n".format(total_appts)
            status = intro + appts_tweet
            imagePath = "../Screenshots/VNACJcapture.png"

            api.update_with_media(imagePath, status)
            print("Appointment(s) found")
            break

    except:
        continue