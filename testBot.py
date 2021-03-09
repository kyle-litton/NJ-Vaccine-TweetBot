import requests
import csv
import time
from bs4 import BeautifulSoup
from playsound import playsound

url = "https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916"

# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')


while True:

    if not soup.find_all("div", {"class": "errormessage"}) and not soup.find_all("div", {"class": "AjaxErrorHandler Popup container component small notoolbar"}):
        playsound('Beep.m4a')
        playsound('Beep.m4a')
        playsound('Beep.m4a')

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
