import requests
import time
import random

'''
{
  "responseMetaData" : {
    "statusCode" : "0000",
    "statusDesc" : "Success",
    "conversationID" : "Id-b1f66560316e37a45ec2bc84",
    "refId" : "Id-b1f66560316e37a45ec2bc84"
  },
  "responsePayloadData" : {
    "schedulerRefType" : "IMZ_STORE",
    "availableDates" : [ "2021-04-02", "2021-04-03", "2021-04-04", "2021-04-05" ],
    "locations" : [ {
      "StoreNumber" : "02284",
      "minuteClinicID" : "0",
      "opticalClinicID" : "0",
      "storeType" : 0,
      "covaxInd" : "Y",
      "pharmacyNCPDPProviderIdentifier" : "3199026",
      "addressLine" : "2545 HOOPER AVE",
      "addressCityDescriptionText" : "BRICK",
      "addressState" : "NJ",
      "addressZipCode" : "08723",
      "addressCountry" : "US",
      "geographicLatitudePoint" : "40.045000",
      "geographicLongitudePoint" : "-74.127300",
      "indicatorStoreTwentyFourHoursOpen" : "N",
      "indicatorPrescriptionService" : "Y",
      "indicatorPhotoCenterService" : "Y",
      "indicatorOpticalService" : "N",
      "instorePickupService" : "N",
      "indicatorDriveThruService" : "Y",
      "indicatorPharmacyTwentyFourHoursOpen" : "N",
      "rxConvertedFlag" : "Y",
      "indicatorCircularConverted" : "Y",
      "indicatorH1N1FluShot" : "N",
      "indicatorRxFluFlag" : "N",
      "indicatorWicService" : "N",
      "snapIndicator" : "Y",
      "indicatorVaccineServiceSupport" : "N",
      "indicatorPneumoniaShotService" : "N",
      "indicatorWeeklyAd" : "Y",
      "indicatorCVSStore" : "Y",
      "indicatorStorePickup" : "N",
      "storeLocationTimeZone" : "EDT",
      "storePhonenumber" : "7329201604",
      "pharmacyPhonenumber" : "7329201604",
      "storeHours" : {
        "DayHours" : [ {
          "Day" : "MON",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "TUE",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "WED",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "THU",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "FRI",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "SAT",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "SUN",
          "Hours" : "08:00 AM - 10:00 PM"
        } ]
      },
      "pharmacyHours" : {
        "DayHours" : [ {
          "Day" : "MON",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "TUE",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "WED",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "THU",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "FRI",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "SAT",
          "Hours" : "09:00 AM - 06:00 PM"
        }, {
          "Day" : "SUN",
          "Hours" : "09:00 AM - 05:00 PM"
        } ]
      },
      "adVersionCdCurrent" : "B",
      "adVersionCdNext" : "B",
      "distance" : "9.56",
      "immunizationAvailability" : {
        "available" : [ "CVD" ],
        "unavailable" : [ ]
      },
      "schedulerRefId" : "CVS_02284",
      "imzAdditionalData" : [ {
        "imzType" : "CVD",
        "availableDates" : [ "2021-04-03" ]
      } ],
      "mfrName" : "Moderna",
      "additionalDoseRequired" : "Y"
    }, {
      "StoreNumber" : "01088",
      "minuteClinicID" : "0",
      "opticalClinicID" : "0",
      "storeType" : 0,
      "covaxInd" : "Y",
      "pharmacyNCPDPProviderIdentifier" : "3133650",
      "addressLine" : "27 MORRISTOWN RD.",
      "addressCityDescriptionText" : "MATAWAN",
      "addressState" : "NJ",
      "addressZipCode" : "07747",
      "addressCountry" : "US",
      "geographicLatitudePoint" : "40.428400",
      "geographicLongitudePoint" : "-74.250700",
      "indicatorStoreTwentyFourHoursOpen" : "N",
      "indicatorPrescriptionService" : "Y",
      "indicatorPhotoCenterService" : "Y",
      "indicatorOpticalService" : "N",
      "instorePickupService" : "Y",
      "indicatorDriveThruService" : "Y",
      "indicatorPharmacyTwentyFourHoursOpen" : "N",
      "rxConvertedFlag" : "Y",
      "indicatorCircularConverted" : "Y",
      "indicatorH1N1FluShot" : "N",
      "indicatorRxFluFlag" : "N",
      "indicatorWicService" : "N",
      "snapIndicator" : "Y",
      "indicatorVaccineServiceSupport" : "N",
      "indicatorPneumoniaShotService" : "N",
      "indicatorWeeklyAd" : "Y",
      "indicatorCVSStore" : "Y",
      "indicatorStorePickup" : "N",
      "storeLocationTimeZone" : "EDT",
      "storePhonenumber" : "7325834347",
      "pharmacyPhonenumber" : "7325834347",
      "storeHours" : {
        "DayHours" : [ {
          "Day" : "MON",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "TUE",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "WED",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "THU",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "FRI",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "SAT",
          "Hours" : "08:00 AM - 10:00 PM"
        }, {
          "Day" : "SUN",
          "Hours" : "08:00 AM - 10:00 PM"
        } ]
      },
      "pharmacyHours" : {
        "DayHours" : [ {
          "Day" : "MON",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "TUE",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "WED",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "THU",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "FRI",
          "Hours" : "09:00 AM - 08:00 PM"
        }, {
          "Day" : "SAT",
          "Hours" : "10:00 AM - 06:00 PM"
        }, {
          "Day" : "SUN",
          "Hours" : "09:00 AM - 05:00 PM"
        } ]
      },
      "adVersionCdCurrent" : "B",
      "adVersionCdNext" : "B",
      "distance" : "20.63",
      "immunizationAvailability" : {
        "available" : [ "CVD" ],
        "unavailable" : [ ]
      },
      "schedulerRefId" : "CVS_01088",
      "imzAdditionalData" : [ {
        "imzType" : "CVD",
        "availableDates" : [ "2021-04-04" ]
      } ],
      "mfrName" : "Pfizer",
      "additionalDoseRequired" : "Y"
    } ]
  }
}


curl 'https://es.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores' \
  -H 'authority: es.cvs.com' \
  -H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
  -H 'accept: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'origin: https://es.cvs.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://es.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: pe=p1; bm_sz=BF9D57EC6C992A776EDEA92B081FC969~YAAQBPs7FyaVg3Z4AQAARa0+jgtXPj1hdJE5h3OnxiipwrOba9rVlV0XF7JMxu96uG7+ug8JqoEPodnxc6SrElsSwXKuqr6xWYLBCl8+fW1INJ+MEcUJnMkYsXCLFKQuSC0sUpUzHuoeUEKYXpnlnMsUe5iTurSQTjUwLVEI+Xf4ZOrgOFXvfeL/BQ0r; ak_bmsc=44569C26F57DEC62D62FF96237ED9357173BFB04FB2300005FF365608CF35E48~plZizyaFYI/kSda72TWPCqkSAGnqAIjKjCG1RdMo3i9m2pcYJg5LR+tMlxyeTFbFKry8uyGr9FeUCyIqKghvcgWHrPZ1zgF627HD/vYllkAcDJW8tk19NkgUIBPrj28IBe3/kWigXMDFvt79aamwWcyEWDgUgcbrjVr9aKEPhy4Ef35MfQ9oRszht6h2uDGRQHbsuqgDb6i531I4RAlgGTOQqnQawQUbY/YJ0cSaXLu4E=; acctdel_v1=on; adh_new_ps=on; adh_ps_pickup=on; adh_ps_refill=on; buynow=off; sab_displayads=on; dashboard_v1=off; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; getcust_elastic=on; echomeln6=on; enable_imz=on; enable_imz_cvd=on; enable_imz_reschedule_instore=on; enable_imz_reschedule_clinic=off; flipp2=on; gbi_cvs_coupons=true; ice-phr-offer=off; v3redirecton=false; mc_cloud_service=on; mc_hl7=on; mc_home_new=off1; mc_ui_ssr=off-p0; memberlite=on; pauth_v1=on; pivotal_forgot_password=off-p0; pivotal_sso=off-p0; pbmplaceorder=off; pbmrxhistory=on; ps=on; refill_chkbox_remove=off-p0; rxdanshownba=off; rxdfixie=on; rxd_bnr=on; rxd_dot_bnr=on; rxdpromo=on; rxduan=on; rxlite=on; rxlitelob=off; rxm=on; rxm_phone_dob=off-p0; rxm_demo_hide_LN=off; rxm_phdob_hide_LN=on; rxm_rx_challenge=off; s2c_akamaidigitizecoupon=on; s2c_beautyclub=off-p0; s2c_digitizecoupon=on; s2c_dmenrollment=off-p0; s2c_herotimer=off-p0; s2c_newcard=off-p0; s2c_papercoupon=on; s2c_persistEcCookie=on; s2c_rewardstrackerbctile=on; s2c_rewardstrackerbctenpercent=on; s2c_rewardstrackerqebtile=on; s2c_smsenrollment=on; s2cHero_lean6=on; sft_mfr_new=on; sftg=on; show_exception_status=on; v2-dash-redirection=on; akavpau_vp_www_cvs_com_vaccine=1617294801~id=8ad9749051895435e854388df2c11976; mc_videovisit=on; CVPF=CT-2; gbi_sessionId=ckmz37vj700003f75djuizle8; gbi_visitorId=ckmz37vj800013f752epzsr49; akavpau_vp_www_cvs_com_vaccine_covid19=1617294818~id=61ff2c1d6c03e1d7b6653b23c0370f34; ADRUM_BT=R:75|i:1684|g:b0bc14af-cc4d-43b7-9ad4-7c8f98d3846e744316|e:292|n:customer1_d6c575ca-3f03-4481-90a7-5ad65f4a5986; bm_sv=8A9CD203EB1A1C1B66F297094CB36A34~busBeItKZ3JRho1dQgJManRbqpiKp0USXyRJRVNXjiyiaJbqqd+cGKKgBvNokDXCIQ+OI2U6pKGy76EBimTG/zf/+06SlXQ/NoVDt4DbVWuk7uY9NSrSUwsKwwx7U26Z9QgzGwIcbkTF79TdB2ibwg==; akavpau_www_cvs_com_general=1617294663~id=3b8d782e48fb40ae91aea7aef5551982; _abck=ACA9EAA20CBE18E2A8F76F69F6CA7F04~0~YAAQ0O4+F+bjXnZ4AQAA1bc/jgUcxbubaP40y3+LwoL7osYKkAKVY6OFSuJNOCEnype/6WKMvSZ1LeXdjdlCWFLBvVcjJZ2FbHbEeA9CJ3twzZ6Mh0pzT7fSjnIUaj+Fo/fJGNWk/4sSP896PbanIhg8mvqSEgEmUN4Qie7hA60VtfO38AZ62aqeoXtaHhkSDUuGjvjcfbQruUU4coQyl7eixInoTmLOGHjPHCiluFP39cEpMePcdikHr3yt6dYa+eNhy6Fxc3iScP/bdY2SsXaXCDY9nUxzms7veT1hVr81cRVePBiTNfYmnEgS1bneskKTYPG1bsmyNz8nt0wBtCePg+6U9JJ+RWJKstrwEjTj0sE75ZxVRJq3A8DDFOGrFOs1o53fY4va9Ypap9elhlwxh9b+~-1~-1~-1' \
  --data-raw '{"requestMetaData":{"appName":"CVS_WEB","lineOfBusiness":"RETAIL","channelName":"WEB","deviceType":"DESKTOP","deviceToken":"7777","apiKey":"a2ff75c6-2da7-4299-929d-d670d827ab4a","source":"ICE_WEB","securityType":"apiKey","responseFormat":"JSON","type":"cn-dep"},"requestPayloadData":{"selectedImmunization":["CVD"],"distanceInMiles":150,"imzData":[{"imzType":"CVD","ndc":["59267100002","59267100003","59676058015","80777027399"],"allocationType":"1"}],"searchCriteria":{"addressLine":"07719"}}}' \
  --compressed

'''

cookies = {
    'pe': 'p1',
    'bm_sz': 'BF9D57EC6C992A776EDEA92B081FC969~YAAQBPs7FyaVg3Z4AQAARa0+jgtXPj1hdJE5h3OnxiipwrOba9rVlV0XF7JMxu96uG7+ug8JqoEPodnxc6SrElsSwXKuqr6xWYLBCl8+fW1INJ+MEcUJnMkYsXCLFKQuSC0sUpUzHuoeUEKYXpnlnMsUe5iTurSQTjUwLVEI+Xf4ZOrgOFXvfeL/BQ0r',
    'ak_bmsc': '44569C26F57DEC62D62FF96237ED9357173BFB04FB2300005FF365608CF35E48~plZizyaFYI/kSda72TWPCqkSAGnqAIjKjCG1RdMo3i9m2pcYJg5LR+tMlxyeTFbFKry8uyGr9FeUCyIqKghvcgWHrPZ1zgF627HD/vYllkAcDJW8tk19NkgUIBPrj28IBe3/kWigXMDFvt79aamwWcyEWDgUgcbrjVr9aKEPhy4Ef35MfQ9oRszht6h2uDGRQHbsuqgDb6i531I4RAlgGTOQqnQawQUbY/YJ0cSaXLu4E=',
    'acctdel_v1': 'on',
    'adh_new_ps': 'on',
    'adh_ps_pickup': 'on',
    'adh_ps_refill': 'on',
    'buynow': 'off',
    'sab_displayads': 'on',
    'dashboard_v1': 'off',
    'db-show-allrx': 'on',
    'disable-app-dynamics': 'on',
    'disable-sac': 'on',
    'dpp_cdc': 'off',
    'dpp_drug_dir': 'off',
    'dpp_sft': 'off',
    'getcust_elastic': 'on',
    'echomeln6': 'on',
    'enable_imz': 'on',
    'enable_imz_cvd': 'on',
    'enable_imz_reschedule_instore': 'on',
    'enable_imz_reschedule_clinic': 'off',
    'flipp2': 'on',
    'gbi_cvs_coupons': 'true',
    'ice-phr-offer': 'off',
    'v3redirecton': 'false',
    'mc_cloud_service': 'on',
    'mc_hl7': 'on',
    'mc_home_new': 'off1',
    'mc_ui_ssr': 'off-p0',
    'memberlite': 'on',
    'pauth_v1': 'on',
    'pivotal_forgot_password': 'off-p0',
    'pivotal_sso': 'off-p0',
    'pbmplaceorder': 'off',
    'pbmrxhistory': 'on',
    'ps': 'on',
    'refill_chkbox_remove': 'off-p0',
    'rxdanshownba': 'off',
    'rxdfixie': 'on',
    'rxd_bnr': 'on',
    'rxd_dot_bnr': 'on',
    'rxdpromo': 'on',
    'rxduan': 'on',
    'rxlite': 'on',
    'rxlitelob': 'off',
    'rxm': 'on',
    'rxm_phone_dob': 'off-p0',
    'rxm_demo_hide_LN': 'off',
    'rxm_phdob_hide_LN': 'on',
    'rxm_rx_challenge': 'off',
    's2c_akamaidigitizecoupon': 'on',
    's2c_beautyclub': 'off-p0',
    's2c_digitizecoupon': 'on',
    's2c_dmenrollment': 'off-p0',
    's2c_herotimer': 'off-p0',
    's2c_newcard': 'off-p0',
    's2c_papercoupon': 'on',
    's2c_persistEcCookie': 'on',
    's2c_rewardstrackerbctile': 'on',
    's2c_rewardstrackerbctenpercent': 'on',
    's2c_rewardstrackerqebtile': 'on',
    's2c_smsenrollment': 'on',
    's2cHero_lean6': 'on',
    'sft_mfr_new': 'on',
    'sftg': 'on',
    'show_exception_status': 'on',
    'v2-dash-redirection': 'on',
    'akavpau_vp_www_cvs_com_vaccine': '1617294801~id=8ad9749051895435e854388df2c11976',
    'mc_videovisit': 'on',
    'CVPF': 'CT-2',
    'gbi_sessionId': 'ckmz37vj700003f75djuizle8',
    'gbi_visitorId': 'ckmz37vj800013f752epzsr49',
    'akavpau_vp_www_cvs_com_vaccine_covid19': '1617294818~id=61ff2c1d6c03e1d7b6653b23c0370f34',
    'ADRUM_BT': 'R:75|i:1684|g:b0bc14af-cc4d-43b7-9ad4-7c8f98d3846e744316|e:292|n:customer1_d6c575ca-3f03-4481-90a7-5ad65f4a5986',
    'bm_sv': '8A9CD203EB1A1C1B66F297094CB36A34~busBeItKZ3JRho1dQgJManRbqpiKp0USXyRJRVNXjiyiaJbqqd+cGKKgBvNokDXCIQ+OI2U6pKGy76EBimTG/zf/+06SlXQ/NoVDt4DbVWuk7uY9NSrSUwsKwwx7U26Z9QgzGwIcbkTF79TdB2ibwg==',
    'akavpau_www_cvs_com_general': '1617294663~id=3b8d782e48fb40ae91aea7aef5551982',
    '_abck': 'ACA9EAA20CBE18E2A8F76F69F6CA7F04~0~YAAQ0O4+F+bjXnZ4AQAA1bc/jgUcxbubaP40y3+LwoL7osYKkAKVY6OFSuJNOCEnype/6WKMvSZ1LeXdjdlCWFLBvVcjJZ2FbHbEeA9CJ3twzZ6Mh0pzT7fSjnIUaj+Fo/fJGNWk/4sSP896PbanIhg8mvqSEgEmUN4Qie7hA60VtfO38AZ62aqeoXtaHhkSDUuGjvjcfbQruUU4coQyl7eixInoTmLOGHjPHCiluFP39cEpMePcdikHr3yt6dYa+eNhy6Fxc3iScP/bdY2SsXaXCDY9nUxzms7veT1hVr81cRVePBiTNfYmnEgS1bneskKTYPG1bsmyNz8nt0wBtCePg+6U9JJ+RWJKstrwEjTj0sE75ZxVRJq3A8DDFOGrFOs1o53fY4va9Ypap9elhlwxh9b+~-1~-1~-1',
}

headers = {
    'authority': 'es.cvs.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://es.cvs.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://es.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"requestMetaData":{"appName":"CVS_WEB","lineOfBusiness":"RETAIL","channelName":"WEB","deviceType":"DESKTOP","deviceToken":"7777","apiKey":"a2ff75c6-2da7-4299-929d-d670d827ab4a","source":"ICE_WEB","securityType":"apiKey","responseFormat":"JSON","type":"cn-dep"},"requestPayloadData":{"selectedImmunization":["CVD"],"distanceInMiles":30,"imzData":[{"imzType":"CVD","ndc":["59267100002","59267100003","59676058015","80777027399"],"allocationType":"1"}],"searchCriteria":{"addressLine":"08723"}}}'

while True:

    response = requests.post('https://es.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores', headers=headers, cookies=cookies, data=data)

    response = response.json()

    if response['responseMetaData']['statusDesc'] == 'Success':
        open_appts = response['responsePayloadData']['locations']

        for x in open_appts:
            print('{0} - {1} - {2}'.format(x['addressCityDescriptionText'],x['addressZipCode'],x['mfrName']))

    elif response['responseMetaData']['statusDesc'] != 'No stores with immunizations found':     
        print(response['responseMetaData']['statusDesc'])


    time.sleep(random.uniform(3.4,4.3))

