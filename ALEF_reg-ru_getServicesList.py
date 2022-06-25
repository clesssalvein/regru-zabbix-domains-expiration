#!/usr/bin/python3
# -*- coding: utf-8 -*-

# modules
import requests
import json
import logging
import sys

# vars
baseUrl = "https://api.reg.ru/api/regru2"

regruAccountUser = sys.argv[1]
regruAccountPass = sys.argv[2]

# request headers
headersSession = {'Content-Type': 'application/json',}

# request session init
try:
    responseSessionInit = requests.get(baseUrl +
                                       '/service/get_list?input_format=json&output_content_type=plain&password=' + regruAccountPass
                                       + '&username=' + regruAccountUser, headers=headersSession)

# pass if error
except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)
    pass

# sessionJson(dict). pycharm 2018 x32 python 3.4
sessionJson = responseSessionInit.json()

# debug
#print(type(sessionJson).__name__)
#print(sessionJson)

# get list of services
servicesList = sessionJson['answer']['services']

# debug
#print(type(list).__name__)
#print(list)

# null string list of services
trunksNamesListJsonForZabbix = ""

# add str data to str json
trunksNamesListJsonForZabbix = (trunksNamesListJsonForZabbix + "{\"data\":[")

# for each service in list
for x in range(len(servicesList)):

    # get dict of services
    serviceDict = servicesList[x]

    # debug
    #print(type(serviceDict).__name__)

    # define vars
    serviceName = serviceDict['dname']
    serviceType = serviceDict['servtype']
    serviceId = serviceDict['service_id']

    # debug
    #print(serviceName + ' ' + serviceType + ' ' + str(serviceId))

    # construct json for zabbix
    trunksNamesListJsonForZabbix = (
                trunksNamesListJsonForZabbix + "{\"{#DOMAINNAME}\"" + ":" + "\"" + serviceName + "\"" + ","
                + "\"{#SERVICETYPE}\"" + ":" + "\"" + serviceType + "\"" + ","
                + "\"{#SERVICEID}\"" + ":" + "\"" + str(serviceId) + "\"" + "}")

    # add coma if not final service in list
    if not x == len(servicesList) - 1:
        trunksNamesListJsonForZabbix = (trunksNamesListJsonForZabbix + ",")

# add final round bracket to json for zabbix
trunksNamesListJsonForZabbix = (trunksNamesListJsonForZabbix + "]}")

# print json of services for zabbix to output
print(trunksNamesListJsonForZabbix)
