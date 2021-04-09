import requests
from harvester import fetch

def harvestToken():
    try:
        while True:
            # block until we get sent a captcha token and repeat
            token = fetch.token('riteaid.com', port=1999)
            return token
    except KeyboardInterrupt:
        pass

def getTimeSlots(storeNum):
    cookies = {
        'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18725%7CMCMID%7C74016139766052224016773531199223648459%7CMCOPTOUT-1617901875s%7CNONE%7CvVersion%7C4.5.1',
        's_sq': 'rtaidglobalproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526link%253DNext%2526region%253Dskip-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dweb%25253Apharmacy%25253Aapt-scheduler%2526pidt%253D1%2526oid%253DNext%2526oidt%253D3%2526ot%253DSUBMIT',
        '__rpck': '0!eyJwcm8iOiJkaXJlY3QiLCJDIjp7fSwiTiI6e30sImR0cyI6MjUuNSwiY3NwIjp7ImIiOjI0NjEwLCJ0IjoyNzYsInNwIjo3MTMzMzMsImMiOjF9fQ~~',
        '__rpckx': '0!eyJ0NyI6eyIzMSI6MTYxNzg5NDYwNzMyMiwiMzIiOjE2MTc4OTQ2MTAwNzMsIjMzIjoxNjE3ODk0NjE1NzI1LCIzNCI6MTYxNzg5NDYzNzcyOX0sInQ3diI6eyIzMSI6MTYxNzg5NDYwNzMyMiwiMzIiOjE2MTc4OTQ2MTAwNzMsIjMzIjoxNjE3ODk0NjE1NzI1LCIzNCI6MTYxNzg5NDYzNzcyOX0sIml0aW1lIjoiMjAyMTA0MDguMTUxMCIsImVjIjoyNH0~',
        's_plt': '1.48',
        's_pltp': 'web%3Apharmacy%3Aapt-scheduler',
        'check': 'true',
        'gpv_Page': 'web%3Apharmacy%3Aapt-scheduler',
        'mbox': 'PC#49e5dadf60bb4eed9d96aed6127a0ea3.34_0#1680713405|session#a9ab3290f93f43e3a7bca360a0db4040#1617896498',
        's_cc': 'true',
        '__rcmp': '0!bj1fZ2MsZj1nYyxzPTAsYz0xNDgsdHI9MCxybj03OTEsdHM9MjAyMTA0MDMuMTY1MCxkPXBj',
        '__ruid': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262',
        '__rutma': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262.1617855175343.1617894607322.7.34.4',
        '__rutmb': '149436981',
        'dtCookie': 'v_4_srv_1_sn_FPV27FLRNNPAJKIFE2QSKD8OE3IR1T4T_app-3Ab52fc261121850f8_1_ol_0_perc_100000_mul_1',
        'dtPC': '1$235575822_910h-vHJEJUDICARIKHHTJMVALNFFKRJDMAIHN-0e1',
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

    params = (
        ('storeNumber', storeNum),
        ('moment', '1617894675061'),
        ('captchatoken', harvestToken()),
    )

    response = requests.get('https://www.riteaid.com/content/riteaid-web/en.ragetavailableappointmentslots.json', headers=headers, params=params, cookies=cookies)

    print(response.content)
    return response.content

getTimeSlots('7822')