import os
import requests

def getStoreInfo():
    cookies = {
        'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18725%7CMCMID%7C74016139766052224016773531199223648459%7CMCOPTOUT-1617862380s%7CNONE%7CvVersion%7C4.5.1',
        '__rpck': '0!eyJwcm8iOiJkaXJlY3QiLCJDIjp7fSwiTiI6e30sImR0cyI6MC41LCJjc3AiOnsiYiI6MjUxNzUsInQiOjI5Nywic3AiOjY3ODExNCwiYyI6MX19',
        's_plt': '2.33',
        's_pltp': 'web%3Apharmacy%3Aapt-scheduler',
        'check': 'true',
        'gpv_Page': 'web%3Apharmacy%3Aapt-scheduler',
        'mbox': 'PC#49e5dadf60bb4eed9d96aed6127a0ea3.34_0#1680713405|session#86b3ae6606be43f08ae130034400b672#1617857036',
        's_cc': 'true',
        's_sq': '%5B%5BB%5D%5D',
        '__rcmp': '0!bj1fZ2MsZj1nYyxzPTAsYz0xNDgsdHI9MCxybj03OTEsdHM9MjAyMTA0MDMuMTY1MCxkPXBj',
        '__rpckx': '0!eyJ0NyI6eyIyNiI6MTYxNzg1NTE3NTM0M30sInQ3diI6eyIyNiI6MTYxNzg1NTE3NTM0M30sIml0aW1lIjoiMjAyMTA0MDguMDQxMiIsImVjIjoxOX0~',
        '__ruid': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262',
        '__rutma': '149436981-pt-1v-4s-1p-k6ofst4caw44h7lvpvxi-1617468604262.1617838969175.1617855175343.6.26.1',
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
    stores = []

    for x in ['07848','07052','08826','08880','08504','08857','07728','08730','07722','08527','08015','08053','08037','08758','08740','08342','08221','08311','08210','08741']:


        params = (
            ('address', x),
            ('attrFilter', 'PREF-112'),
            ('fetchMechanismVersion', '2'),
            ('radius', '50'),
        )

        response = requests.get('https://www.riteaid.com/services/ext/v2/stores/getStores', headers=headers, params=params, cookies=cookies)

        data = response.json()['Data']['stores']

        '''

        PREF-113 - Moderna
        PREF-114 - Pfizer
        PREF-115 - Johnson & Johnson

        '''

        for x in data:
            if x['state'] == 'NJ':
                vaxTypes = x['specialServiceKeys']
                if 'PREF-113' in vaxTypes:
                    vax = 'Moderna'
                elif 'PREF-114' in vaxTypes:
                    vax = 'Pfizer'
                elif 'PREF-115' in vaxTypes:
                    vax = 'Johnson & Johnson'
                else:
                    vax = ''
                stores.append((str(x['storeNumber']), str(x['address']), str(x['city']), str(x['zipcode']), vax))
    
    return sorted(set(stores),key=lambda x: x[2])
