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

'''

NO LONGER IN USE. Site moved to registration link.

'''

key_file = '../keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

url = "https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656&code=njv&vt=112916"

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--window-size=1200,824")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options,executable_path='../Drivers/chromedriver')

# Set up clear cache
send_command = ('POST', '/session/$sessionId/chromium/send_command')
driver.command_executor._commands['SEND_COMMAND'] = send_command

HMHN_Timer = 0

print("Searching for appointments...")
while True:
    #print('\n')

    try:
        driver.delete_all_cookies()
        driver.execute('SEND_COMMAND', dict(cmd='Network.clearBrowserCache', params={}))
        driver.get(url)
        time.sleep(random.uniform(1.4,2.4))
    except:
        time.sleep(random.uniform(120,150))
        #print("URL Did not load.")
        continue

    # Check if the main tag is there, avoids the high traffic page and makes the other tags readable
    try:
        mainFrame = WebDriverWait(driver, random.uniform(1.7,2.2)).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]'))
        )
    except:
        time.sleep(random.uniform(3.2,4.6))
        #print("No main tag.")
        continue
    
    # Find the OpeningsData div, used to check whether any open appointments
    try:
        element = WebDriverWait(driver, random.uniform(1.7,2.2)).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="D6F73C26-7627-4948-95EA-2C630C25C5E9_scheduleOpenings_OpeningsData"]'))
    )
    except:
        #print("No openings Data Div")
        continue


    # Final check to make sure there are appointments and no loading heart
    try:
        slotList = driver.find_element_by_xpath('//*[@id="D6F73C26-7627-4948-95EA-2C630C25C5E9_scheduleOpenings_OpeningsData"]/div/div/div[4]/div/div')
        if slotList.get_attribute("class") == 'slotslist hasScrollIndicator':
 
            driver.get_screenshot_as_file("../Screenshots/HMHNcapture.png")
            imagePath = "../Screenshots/HMHNcapture.png"
            

            if time.time() - HMHN_Timer > 240 or HMHN_Timer == 0:

                # Get num appointments
                numAppointments = len(set(slotList.find_elements_by_tag_name('a')))

                if numAppointments > 1:
                    status = 'Hackensack Meridian: {0} time slots available, https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656&code=njv&vt=112916 \n\nChoose guest, use auto-fill, and select no insurance to complete the form ASAP! Keep refreshing!'.format(numAppointments)
                    try:
                        err_popup_msg = driver.find_element_by_xpath('/html/body/div[14]/div[2]/div/div[1]/p')
                        print(err_popup_msg.text)
                        continue
                    except:
                        HMHN_Timer = time.time()
                        api.update_with_media(imagePath, status)
                        print('{0} appointment(s) found.'.format(numAppointments))
                else:
                    status = 'Hackensack Meridian: 1 Cancellation found at this link, https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656&code=njv&vt=112916 \n\nCancellations go VERY quickly, good luck!!'
                    try:
                        err_popup_msg = driver.find_element_by_xpath('/html/body/div[14]/div[2]/div/div[1]/p')
                        print(err_popup_msg.text)
                        continue
                    except:
                        HMHN_Timer = time.time()
                        api.update_with_media(imagePath, status)
                        print('{0} appointment(s) found.'.format(numAppointments))   

            continue
        #print("Slotlist has no scroll indicator")

    except:
        #print("Slotlist not found")
        continue