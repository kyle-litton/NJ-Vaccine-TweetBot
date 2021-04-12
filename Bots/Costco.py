from Utils.GetCostcoInfo import *
from Utils.CreatePhoto import build
import json
import tweepy
import time
import random
from tqdm import tqdm

'''

The request used here can be found open to the public on the Costco Vaccine (https://book.appointment-plus.com/d138ktz8/#/) website.
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

total = 0
pic_len = 0
openLocations = ''
stores = getCostcoStores()

print('Searching for any open appointments...')
while True:

    openStores = 0
    for store in tqdm(stores):
        
        eId = getEiD(store[0])
        vaxInfo = getVaccineType(store[0],eId)
        slots = getTimeSlots(eId,vaxInfo[0])

        available = 0
        if len(slots) > 0:
            openStores += 1

            # iterate through every available day at this location
            for key in slots.keys():
                totalSpots = slots[key]['timeSlots']['numberOfSpots']
                takenSpots = slots[key]['timeSlots']['numberOfSpotsTaken']

                for i in range(len(totalSpots)):
                    available += totalSpots[i] - takenSpots[i]
            total += available

            pic_len += 45
            openLocations += store[1] + ', ' + store[2] + ':  (' + str(available) + ' available appointments) : ' + vaxInfo[1] + '\n\n'


    if total > 0 and openLocations != '':
        imagePath = build(openLocations, 750, pic_len, '../Screenshots/CostcoCapture.png')
        status = '{0} Costco location(s) showing a total of {1} appointment(s) available.\n\nCheck here: https://book.appointment-plus.com/d138ktz8/#/\n\nRefer to the attached photo for details on locations, availablity, and vaccine type.'.format(openStores,total)

        api.update_with_media(imagePath, status)
        print(status)
        exit()

    time.sleep(random.uniform(8.4, 15.6))
