import os
import requests

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

nj_storeNums = ['10488', '4746', '10429', '2518', '4509', '10424', '1796', '3477', '1970', '10517', '10512', '10487', '4812', '10436', '1661', '3427', '425', '3974', '10510', '220', '10496', '1917', '4045', '599', '994', '7935', '1866', '1870', '4819', '1778', '10427', '1736', '116', '2561', '1654', '4821', '407', '10467', '10442', '10463', '7822', '10435', '219']

for x in nj_storeNums:


    params = (
        ('storeNumber', x),
    )

    response = requests.get('https://www.riteaid.com/services/ext/v2/vaccine/checkSlots', headers=headers, params=params, cookies=cookies)


    print(response.json()['Data']['slots'])
