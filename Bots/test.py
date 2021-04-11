import json
slots = json.loads('{"2021-04-15": {"timeSlots": {"numberOfSpots": [2], "numberOfSpotsTaken": [1], "startTimestamp": ["11:45:00"], "endTimestamp": ["12:00:00"]}}}')

available = 0
# iterate through every available day at this location
for key in slots.keys():
    totalSpots = slots[key]['timeSlots']['numberOfSpots']
    takenSpots = slots[key]['timeSlots']['numberOfSpotsTaken']

    for x in range(len(totalSpots)):
        available += totalSpots[x] - takenSpots[x]
    print(available)

