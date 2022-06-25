#!/usr/bin/python3
# -*- coding: utf-8 -*-

# modules
import requests
import json
import logging
from datetime import datetime
import sys

# vars
dateCurrentEpoch = datetime.today().timestamp()
baseUrl = "https://api.reg.ru/api/regru2"

regruAccountUser = sys.argv[1]
regruAccountPass = sys.argv[2]
serviceId = sys.argv[3]


# request headers
headersSession = {'Content-Type': 'application/json',
                          }

try:
    # request session init
    responseSessionInit = requests.get(baseUrl +
                                       '/service/get_info?input_data={"services":[{"service_id": "' + serviceId + '"}]}&input_format=json&output_content_type=plain&password=' + regruAccountPass
                                       + '&username=' + regruAccountUser, headers=headersSession)

# pass if error
except Exception as e:
    #logging.error('Error at %s', 'division', exc_info=e)
    pass

# sessionJson(dict). pycharm 2018 x32 python 3.4
try:
    sessionJson = responseSessionInit.json()
# pass if error
except Exception as e:
    #logging.error('Error at %s', 'division', exc_info=e)
    pass

# debug
#print(type(sessionJson).__name__)
#print(sessionJson)

if ('sessionJson' in globals()) and ((type(sessionJson) == dict)):

    # get list of services
    serviceInfoList = sessionJson['answer']['services']

    # for each service in list
    for x in range(len(serviceInfoList)):

        # get dict of services
        serviceInfoDict = serviceInfoList[x]
        serviceExpirationDate = serviceInfoDict['expiration_date']

        # convert human expiration date to epoch
        if not (serviceExpirationDate == "0000-00-00"):
            serviceExpirationDateEpoch = datetime.strptime(serviceExpirationDate, "%Y-%m-%d").timestamp()

            # debug
            #print(dateCurrentEpoch)
            #print(serviceExpirationDateEpoch)

            # calc service time left
            serviceTimeLeft = (serviceExpirationDateEpoch-dateCurrentEpoch)

            # ouput service time left
            print(serviceTimeLeft)
        else:
            # ouput service time left
            print("999999999")
