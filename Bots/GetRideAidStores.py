import os
import requests

cookies = {
    'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18720%7CMCMID%7C69022973536707866352095779083048215874%7CMCOPTOUT-1617415347s%7CNONE%7CvVersion%7C4.5.1',
    's_cc': 'true',
    's_plt': '1.91',
    's_pltp': 'web%3Apharmacy%3Aapt-scheduler',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'gpv_Page': 'web%3Apharmacy%3Aapt-scheduler',
    'mbox': 'session#44fbc0f9da684752a2bfeaabb82f5786#1617409997|PC#44fbc0f9da684752a2bfeaabb82f5786.34_0#1680652117',
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

stores = []

for x in ['08807','08723','Atlantic City', 'Vineland','Sparta','Hoboken',]:


    params = (
        ('address', x),
        ('attrFilter', 'PREF-112'),
        ('fetchMechanismVersion', '2'),
        ('radius', '50'),
    )

    response = requests.get('https://www.riteaid.com/services/ext/v2/stores/getStores', headers=headers, params=params, cookies=cookies)

    data = response.json()['Data']['stores']

    for x in data:
        if x['state'] == 'NJ':
            stores.append(str(x['storeNumber']) + ' ' + str(x['city']))

print(set(stores))