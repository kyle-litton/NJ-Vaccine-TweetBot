import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tqdm import tqdm

def getCostcoStores():
        
    cookies = {
        'sess_prod-spark-ap': 'eyJpdiI6IlZcLzBvXC9qRHZYd1wvZENQM3Y3Vm01aUE9PSIsInZhbHVlIjoiQU81N043MGdMbmgxcVAxbWxOdWF0TVpcLzdETWpvZUgxNHZrdXpYSkRmWFJORXZiNitYTW43amZXeEdTdlQ5dlJBNVBPSGJSeWlrSlBMMXF1XC9hdHY2UT09IiwibWFjIjoiMGFkODZkYjU4NmM5ODFmYjhjYWZlZDYxZDI4ODBiYzFjNmIyMDhkNWJjZDFlNTY2MWRkZmZkNTRhY2U2ZDJjYSJ9',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-us',
        'Host': 'book.appointment-plus.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Referer': 'https://book.appointment-plus.com/d138ktz8/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }

    storeInfo = []

    for page in ['1','2','3']:


        params = (
            ('clientMasterId', '426227'),
            ('pageNumber', page),
            ('itemsPerPage', '10'),
            ('keyword', ''),
            ('clientId', ''),
            ('employeeId', ''),
            ('centerCoordinates[id]', ''),
            ('centerCoordinates[latitude]', '40.150534799999996'),
            ('centerCoordinates[longitude]', '-74.0447003'),
            ('centerCoordinates[accuracy]', '17629'),
            ('centerCoordinates[whenAdded]', ''),
            ('centerCoordinates[searchQuery]', ''),
            ('radiusInKilometers', '100'),
            ('_', '1617991914528'),
        )

        response = requests.get('https://book.appointment-plus.com/book-appointment/get-clients', headers=headers, params=params, cookies=cookies)

        data = response.json()['clientObjects']

        for store in tqdm(data):
            if store['state'] == 'NJ':
                eId = getEiD(str(store['id']),str(store['clientMasterId']))
                if eId != 'Error':
                    storeInfo.append((str(store['id']),str(store['address1']),str(store['city']),str(eId),str(store['clientMasterId'])))

    return storeInfo

def getVaccineType(storeId,eId,cId):
    cookies = {
    'sess_prod-spark-ap': 'eyJpdiI6IklZNVVqVG1oWldCbjBKYWhXcUJrXC93PT0iLCJ2YWx1ZSI6Ik5RUWFyRjFQalI2ZDhPdXBXSGdCQVVTdUNLYU1mN1QzUUZicHd5N1lJdGdLcjhsbVdnbEl5dnhaZ1wvZTluUFdRUlFHeERITGRSQTFHVUpjblBSWGp2QT09IiwibWFjIjoiYzFlOWFjYjYxZTFiYjUyNTk2YWZjNGNjNzI1OGIwZDE2ZDBlY2ZlYzEyOTgzYTNiOGE0NzgzYTE4ZmM5YmI1NCJ9',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-us',
        'Host': 'book.appointment-plus.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Referer': 'https://book.appointment-plus.com/d138ktz8/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = (
        ('clientMasterId', cId),
        ('clientId', storeId),
        ('pageNumber', '1'),
        ('itemsPerPage', '10'),
        ('keyword', ''),
        ('serviceId', ''),
        ('_', '1617991914539'),
    )

    response = requests.get('https://book.appointment-plus.com/book-appointment/get-services/{0}'.format(eId), headers=headers, params=params, cookies=cookies)
    data = response.json()
    data = data['serviceObjects']
    VaccineId = data[0]['id']
    VaccineName = data[0]['serviceDetails']['title']
    return (VaccineId,VaccineName)

def getEiD(storeId,cId):
    # 'Employee Id' used in finding open appointments, not sure why they named it that
    # Seems like they have one default per store. 

    cookies = {
    'sess_prod-spark-ap': 'eyJpdiI6IlwvcVpwY00rUkZwbERPZWcxNzdHbUZBPT0iLCJ2YWx1ZSI6ImNOdThKc1IySTBmdmt2Vk9GZ0NSSVFOMEIzaTBlcmQwckFLMTRPR1ZtR3lqRDRwWUpxWnphOWY4dkhcL2JTa3M4UGh1aVBWY0tcLzRNeHBKbEQ1cnkrQ1E9PSIsIm1hYyI6IjNjYmFlOGRmMTFhZTljMGVlZjRmMjkwYjBkZTZiMDYxYjljMDZlNjZhYmNiZGU1YmQ5ZTFjNzgxMDUxMTU0MzkifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-us',
        'Host': 'book.appointment-plus.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Referer': 'https://book.appointment-plus.com/d138ktz8/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = (
        ('clientMasterId', cId),
        ('clientId', storeId),
        ('pageNumber', '1'),
        ('itemsPerPage', '10'),
        ('keyword', ''),
        ('employeeId', ''),
        ('_', '1617994212527'),
    )

    response = requests.get('https://book.appointment-plus.com/book-appointment/get-employees', headers=headers, params=params, cookies=cookies)
    data = response.json()
    
    data = data['employeeObjects']

    try:
        return str(data[0]['id'])
    except:
        return 'Error'

def getTimeSlots(eId, vaxCode, cId):
    cookies = {
    'sess_prod-spark-ap': 'eyJpdiI6InFqbnpXK1I0c0I3Q1wvT09yV3lkcXhBPT0iLCJ2YWx1ZSI6ImNUR1VndHJOUkJLc1BtTmQ5Z0Q0dVJzVks3eXc0bEl0TVgwcERVaXRuWGRpWjVrQlRIQXc4NldheXBXYld3MkpFbFM2XC9kYjk2c2k4QzdMRkdDQjlqdz09IiwibWFjIjoiMTYwNDdkYzk1MDUwMzg2MDZjZTg5ZjgyMjg0ZmNmZmIzMTQzZjhkMDU4ZjdhN2QzZDNlYjg4OTIyOWUxODE4MSJ9',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-us',
        'Host': 'book.appointment-plus.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Referer': 'https://book.appointment-plus.com/d138ktz8/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }

    endTime = datetime.now() + relativedelta(months=+1)
    endTime = endTime.strftime("%Y-%m-%d %H:%M:%S")

    params = (
        ('startTimestamp', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        ('endTimestamp', endTime),
        ('limitNumberOfDaysWithOpenSlots', '3'),
        ('employeeId', eId),
        ('services[]', vaxCode),
        ('numberOfSpotsNeeded', '1'),
        ('isStoreHours', 'true'),
        ('clientMasterId', cId),
        ('toTimeZone', 'false'),
        ('fromTimeZone', '149'),
        ('_', '1617995992649'),
    )

    response = requests.get('https://book.appointment-plus.com/book-appointment/get-grid-hours', headers=headers, params=params, cookies=cookies)
    data = response.json()['data']
    timeSlots = data['gridHours']
    return timeSlots
