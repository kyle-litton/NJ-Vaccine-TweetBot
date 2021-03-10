import requests
import time
import tweepy
from playsound import playsound
from bs4 import BeautifulSoup

import json
key_file = 'keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

hmhn_URL = "https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"
hmhn_timer = 0

# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

page = requests.get(hmhn_URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
checkStr = "Please check back in a bit."

while True:

    if soup.find_all("div", {"class": "slotslist hasScrollIndicator"}):
        # Appointments Open -- Post Tweet
        
        if time.time() - hmhn_timer > 480 or hmhn_timer == 0: 
            # Test Beeps
            #playsound('Beep.m4a')
            #playsound('Beep.m4a')
            #playsound('Beep.m4a')

            api.update_status("Hackensack Meridian: Portal is open at this link https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916")
            hmhn_timer = time.time()
            print(f"HMHN Appointment found at {hmhn_timer}")
    try:
        page = requests.get(hmhn_URL, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        time.sleep(3)
        continue
    