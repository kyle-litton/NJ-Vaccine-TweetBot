import os
import requests
import tweepy
import json
import time
import random
from Utils.GetRiteAidStores import getStoreInfo
from Utils.CreatePhoto import build

'''

The below request can be found open to the public on the Rite Aid website.
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

cookies = {
    'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18725%7CMCMID%7C74016139766052224016773531199223648459%7CMCOPTOUT-1617847231s%7CNONE%7CvVersion%7C4.5.1',
    's_sq': 'rtaidglobalproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526link%253DSELECT%252520THIS%252520STORE%2526region%253Dskip-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.riteaid.com%25252Fpharmacy%25252Fapt-scheduler%252523%2526ot%253DA',
    '__rpckx': '0!eyJ0NyI6eyIxMyI6MTYxNzgzNTU3MzA0MywiMTQiOjE2MTc4MzU1OTc5OTAsIjE1IjoxNjE3ODM1NjA2MDEyLCIxNiI6MTYxNzgzNTYyODk1NSwiMTkiOjE2MTc4MzU5ODAyMDcsIjIwIjoxNjE3ODM2NDIyMDQyLCIyMSI6MTYxNzgzNjUwNDUwMCwiMjIiOjE2MTc4Mzg5NjkxNzUsIjIzIjoxNjE3ODM4OTcxMjgwLCIyNCI6MTYxNzgzODk3NjM0OCwiMjUiOjE2MTc4MzkwMDI2NTV9LCJ0N3YiOnsiMTMiOjE2MTc4MzU1NzMwNDMsIjE0IjoxNjE3ODM1NTk3OTkwLCIxNSI6MTYxNzgzNTYwNjAxMiwiMTYiOjE2MTc4MzU2OTc5MjAsIjE5IjoxNjE3ODM2NDAwMjIxLCIyMCI6MTYxNzgzNjQ4MjA2MSwiMjEiOjE2MTc4Mzg5MjI5NjcsIjIyIjoxNjE3ODM4OTY5MTc1LCIyMyI6MTYxNzgzODk3MTI4MCwiMjQiOjE2MTc4Mzg5NzYzNDgsIjI1IjoxNjE3ODQwMDE0NTcxfSwiaXRpbWUiOiIyMDIxMDQwNy4yMzQyIiwiZWMiOjE5fQ~~',
    '__rpck': '0!eyJwcm8iOiJkaXJlY3QiLCJDIjp7fSwiTiI6e30sImR0cyI6MC41LCJjc3AiOnsiYiI6MjUxNzUsInQiOjI5Nywic3AiOjY3ODExNCwiYyI6MX19',
    's_plt': '2.57',
    's_pltp': 'web%3Apharmacy%3Aapt-scheduler',
    's_cc': 'true',
    'check': 'true',
    'gpv_Page': 'web%3Apharmacy%3Aapt-scheduler',
    'mbox': 'PC#49e5dadf60bb4eed9d96aed6127a0ea3.34_0#1680713405|session#54877ddc529740c4920e226862da86c9#1617840863',
    '__rcmp': '0!bj1fZ2MsZj1nYyxzPTAsYz0xNDgsdHI9MCxybj03OTEsdHM9MjAyMTA0MDMuMTY1MCxkPXBj',
    '__ruid': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262',
    '__rutma': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262.1617835573043.1617838969175.5.25.4',
    '__rutmb': '149436981',
    'dtCookie': 'v_4_srv_1_sn_FPV27FLRNNPAJKIFE2QSKD8OE3IR1T4T_app-3Ab52fc261121850f8_1_ol_0_perc_100000_mul_1',
    'dtSa': '-',
    'PHPSESSID': '0d0d2931d1bdb8a0111be243b922724b',
    'form_key': 'iaBO9XBnUViKR0Vb',
    'wp_customerGroup': 'NOT+LOGGED+IN',
    'section_data_ids': '%7B%22cart%22%3A1617835584%2C%22prop65%22%3A1617835577%7D',
    'rxVisitor': '1617835575825OGGR3U2N6L98K20FA513JH6L18U13ABF',
    'mage-messages': '',
    'product_data_storage': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'rxvt': '1617837375908|1617835575826',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'AMCVS_3B2A35975CF1D9620A495FA9%40AdobeOrg': '1',
    '_elevaate_session_id': '86705921-2eab-42b9-b4a1-d96fe3dd5d5e',
    '_fbp': 'fb.1.1617480690368.605267682',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-us',
    'Host': 'www.riteaid.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Referer': 'https://www.riteaid.com/pharmacy/apt-scheduler',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
}


nj_stores = getStoreInfo()

openLocations = ''
Tweet_Timer = 0
pic_len = 0
cur_open = 0
lastOpen = 0


newOpenings = False

for x in nj_stores:
    
    store = x[1] + ', ' + x[2] + ' -- ' + x[3] + ' -- ' + x[4] + '\n\n'

    params = (
        ('storeNumber', x[0]),
    )

    response = requests.get('https://www.riteaid.com/services/ext/v2/vaccine/checkSlots', headers=headers, params=params, cookies=cookies)

    try:
        data = response.json()['Data']['slots']
    except:
        print('API Timed out')
        time.sleep(random.uniform(100.4, 180.6))
        continue
    
    if data['1'] == True or data['2'] == True:
        if store not in openLocations:
            openLocations += store
            cur_open += 1
            pic_len += 40
            newOpenings = True
            
    elif store in openLocations:
        openLocations = openLocations.replace(store, '')
        cur_open -= 1
        pic_len -= 40
        
if openLocations != '':

    imagePath = build(openLocations,550,pic_len, '../Screenshots/RiteAidcapture.png')

    status = '{0} Rite Aid locations are showing some availablity.\n\nCheck here: https://www.riteaid.com/covid-vaccine-apt\n\nThese can be hit or miss, try going through each zipcode from the attached image.'.format(cur_open)

    if (time.time() - Tweet_Timer > 250 or Tweet_Timer == 0 or cur_open > lastOpen+3) and newOpenings == True:
        #api.update_with_media(imagePath, status)
        print(openLocations)
        print('{0} / {1} stores are showing some availablity.'.format(cur_open, len(nj_stores)))
        Tweet_Timer = time.time()
        lastOpen = cur_open

else:
    print('No stores are open.')