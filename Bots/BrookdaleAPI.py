import requests

headers = {
    'authority': 'api.blockitnow.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': '*/*',
    'authorization': '',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://app.blockitnow.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://app.blockitnow.com/',
    'accept-language': 'en-US,en;q=0.9',
}

data = '${"operationName":"GetConsumerSchedulingProfileSlotsQuery","variables":{"profileId":"3d39093d-3f89-4817-bec1-862e388eba1a","procedureId":"bcb048c9-21ce-4233-a3b9-83566f5b1d0f","start":"2021-04-12","end":"2021-04-18"},"query":"query GetConsumerSchedulingProfileSlotsQuery($procedureId: ID\\u0021, $profileId: ID\\u0021, $start: String, $end: String) {\\n getConsumerSchedulingProfileSlots(procedureId: $procedureId, profileId: $profileId, start: $start, end: $end) {\\n id\\n start\\n end\\n status\\n slotIdsForAppointment\\n     __typename\\n }\\n}\\n"}'

response = requests.post('https://api.blockitnow.com/', headers=headers, data=data)



print(response.json())