import requests
from PIL import Image, ImageDraw, ImageFont

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

response = requests.get('https://s3-us-west-2.amazonaws.com/mhc.cdn.content/vaccineAvailability.json', headers=headers, params=params)

data = response.json()

locations = ''
for x in data:
    if 'NJ' in x['address'] and x['availability'] == 'yes':
        locations += x['address'] + '\n'

img = Image.new('RGB', (400, 500), color = 'white')
 
d = ImageDraw.Draw(img)
font = ImageFont.truetype('../Drivers/Roboto-Black.ttf')
d.text((10,10), locations, fill='black',font=font)
 
img.save('../Screenshots/ACMEcapture.png')
