import requests
from PIL import Image, ImageDraw, ImageFont
import tweepy
import json

'''

The below request can be found open to the public on the Acme scheduler website.
When using the scheduler, look at network traffic in the browser.
Right click on the endpoint request that loads available appointments.
Choose copy as cURL, then convert to a python request. The cookies may
expire over time.

'''

key_file = '../keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Origin': 'https://www.mhealthappointments.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.mhealthappointments.com/',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('v', '1617383002336'),
)

#response = requests.get('https://s3-us-west-2.amazonaws.com/mhc.cdn.content/vaccineAvailability.json', headers=headers, params=params)

data = response.json()

locations = ''
pic_len = 0
cur_open = 0
for x in data:
    if 'NJ' in x['address'] and x['availability'] == 'yes':
        store = x['address'].split('-')[1]
        locations += store + '\n\n'
        cur_open += 1
        pic_len += 40

print(cur_open)
img = Image.new('RGB', (400, pic_len), color = 'white')
 
d = ImageDraw.Draw(img)
font = ImageFont.truetype('../Drivers/Roboto-Black.ttf',15)
d.text((10,10), locations, fill='black',font=font)
 
img.save('../Screenshots/ACMEcapture.png')

imagePath = '../Screenshots/ACMEcapture.png'

status = '{0} Acme locations are showing some availablity.\n\nCheck here: https://www.mhealthappointments.com/covidappt\n\nIf none are open check back again until it shows none available.'.format(cur_open)

#if cur_open > 0:
    #api.update_with_media(imagePath, status)