import os
import requests
from PIL import Image, ImageDraw, ImageFont
import tweepy
import json
import time
import random

key_file = '../keys.json'
with open(key_file) as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)

cookies = {
    'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18720%7CMCMID%7C69022973536707866352095779083048215874%7CMCOPTOUT-1617414870s%7CNONE%7CvVersion%7C4.5.1',
    's_sq': 'rtaidglobalproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526link%253DSELECT%252520THIS%252520STORE%2526region%253Dskip-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.riteaid.com%25252Fpharmacy%25252Fapt-scheduler%252523%2526ot%253DA',
    's_cc': 'true',
    's_plt': '3.68',
    's_pltp': 'web%3Apharmacy%3Aapt-scheduler',
    'gpv_Page': 'web%3Apharmacy%3Aapt-scheduler',
    'check': 'true',
    'mbox': 'session#44fbc0f9da684752a2bfeaabb82f5786#1617409482|PC#44fbc0f9da684752a2bfeaabb82f5786.34_0#1680652117',
    'dtCookie': 'v_4_srv_1_sn_QBHRFCLU7CVFEE763VL96EEA9DLSV6A0_app-3Ab52fc261121850f8_0_ol_0_perc_100000_mul_1',
    'rxVisitor': '1617407540586O0UICRNEGEL3K1VP1HJ9HPKGDPQ63VPD',
    'rxvt': '1617409341113|1617407540588',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'dtLatC': '1',
    'dtSa': 'false%7C_load_%7C1%7C_load_%7C-%7C1617407540140%7C407540582_148%7Chttps%3A%2F%2Fwww.riteaid.com%2Fshop%2Fminicart%2Finterop%7C%7C%7C%7C',
    'currentStore': 'eyJzdG9yZU51bWJlciI6IjAwNDA3IiwiYWRkcmVzcyI6IjM2NiBHZW9yZ2UgU3RyZWV0IiwiY2l0eSI6Ik5ldyBCcnVuc3dpY2siLCJzdGF0ZSI6Ik5KIiwiemlwY29kZSI6IjA4OTAxIn0%3D',
    'AMCVS_3B2A35975CF1D9620A495FA9%40AdobeOrg': '1',
    '_elevaate_session_id': '0e1859ec-a9d1-445d-ac2b-c8ac7da8126e',
    'wp_customerGroup': 'NOT+LOGGED+IN',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-us',
    'Host': 'www.riteaid.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Referer': 'https://www.riteaid.com/pharmacy/apt-scheduler',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
}

nj_storeNums = [('1661', '2859-61 Kennedy Boulevard', 'Jersey City', '07306'), ('116', '907 North High Street', 'Millville', '08332'), ('10424', '75 South Main Street', 'Neptune', '07753'), ('10488', '970 North Main Road', 'Vineland', '08360'), ('1870', '531 Us Highway 22 East', 'Whitehouse Station', '08889'), ('1970', '431 Haledon Avenue', 'Haledon', '07508'), ('2561', '332 Raritan Avenue', 'Highland Park', '08904'), ('4819', '1881 North Black Horse Pike', 'Williamstown', '08094'), ('7822', '2791 S Delsea Drive', 'Vineland', '08360'), ('1654', '5 Lafayette Road', 'Fords', '08863'), ('10496', '1 North New Prospect Road', 'Jackson', '08527'), ('4821', '10 Lincoln Highway', 'Edison', '08820'), ('10435', '213 South Street', 'Morristown', '07960'), ('2518', '159 East Kennedy Boulevard', 'Lakewood', '08701'), ('7935', '416 Route 1', 'Edison', '08817'), ('3974', '1041 Burnt Tavern Road', 'Brick', '08724'), ('10442', '695 North Delsea Drive', 'Glassboro', '08028'), ('219', '123 East Main Street Suite 16', 'Denville', '07834'), ('10427', '151 Route 94', 'Blairstown', '07825'), ('3427', '237 Spring Street', 'Newton', '07860'), ('4509', '353 Us Highway 202/206', 'Bridgewater', '08807'), ('4812', '981 West Side Avenue', 'Jersey City', '07306'), ('10436', '186 South White Horse Pike', 'Berlin', '08009'), ('4045', '1434 S Black Horse Pike', 'Williamstown', '08094'), ('3477', '773 Hamilton Street', 'Somerset', '08873'), ('10429', '203 Mountain Avenue', 'Hackettstown', '07840'), ('220', '2 Upper Sarepta Road', 'Belvidere', '07823'), ('425', '3258 Bridge Avenue', 'Point Pleasant', '08742'), ('1736', '1366 Clifton Avenue', 'Clifton', '07012'), ('4746', '132 North Gaston Avenue', 'Somerville', '08876'), ('10467', '677 Cross Keys Road', 'Sicklerville', '08081'), ('10463', '403 Sicklerville Road', 'Sicklerville', '08081'), ('1796', '4057 Asbury Ave Ste 8', 'Tinton Falls', '07753'), ('10487', '7 West Landis Avenue', 'Vineland', '08360'), ('1866', '375  White Horse Pike', 'Atco', '08004'), ('10512', '811 Fischer Boulevard', 'Toms River', '08753'), ('10517', '86  B Lacey Road', 'Whiting', '08759'), ('994', '480 North Beverwyck Road', 'Lake Hiawatha', '07034'), ('1917', '236 South Delsea Drive', 'Clayton', '08312'), ('599', '841 Georges Road', 'North Brunswick', '08902'), ('407', '366 George Street', 'New Brunswick', '08901'), ('10510', '149 Main Street', 'Manasquan', '08736'), ('1778', '596 Shrewsbury Avenue', 'Tinton Falls', '07701')]

openLocations = ''
Tweet_Timer = 0
pic_len = 0
cur_open = 0
lastOpen = 0

while True:
    newOpenings = False
    time.sleep(random.uniform(2.8,3.7))
    
    for x in nj_storeNums:
        
        store = x[1] + ', ' + x[2] + ' -- ' + x[3] + '\n\n'

        params = (
            ('storeNumber', x[0]),
        )

        response = requests.get('https://www.riteaid.com/services/ext/v2/vaccine/checkSlots', headers=headers, params=params, cookies=cookies)
        data = response.json()['Data']['slots']

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
        

    img = Image.new('RGB', (450, pic_len), color = 'white')
    
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('../Drivers/Roboto-Black.ttf',15)
    d.text((10,10), openLocations, fill='black',font=font)
    
    img.save('../Screenshots/RiteAidcapture.png')

    imagePath = '../Screenshots/RiteAidcapture.png'

    status = '{0} Rite Aid locations are showing some availablity.\n\nCheck here: https://www.riteaid.com/covid-vaccine-apt\n\nCheck back later if none are available.'.format(cur_open)

    if (time.time() - Tweet_Timer > 250 or Tweet_Timer == 0 or cur_open > lastOpen+3) and newOpenings == True:
        api.update_with_media(imagePath, status)
        print(status)
        print('\n')
        Tweet_Timer = time.time()
        lastOpen = cur_open