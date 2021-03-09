import requests
import time
import tweepy
from bs4 import BeautifulSoup

import json
key_file = 'keys.json'
with open(key_file) as f:
    keys = json.load(f)

url = "https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"

# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')


while True:

    if not soup.find_all("div", {"class": "errormessage"}) and not soup.find_all("div", {"class": "AjaxErrorHandler Popup container component small notoolbar"}):
        # Appointments Open -- Post Tweet
        
        auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        api = tweepy.API(auth)

        api.update_status("Hackensack Meridian: Portal is open at this link https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916")

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')