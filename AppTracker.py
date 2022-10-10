#!/usr/bin/env python3
import argparse
from enum import Enum
import json
import sys

# Enum to represent the status of an application
class appStatus(str, Enum):
    NOAPP = 'NOAPP'
    APP = 'APP'
    REJ = 'REJ'
    MORE = 'MORE'
    INTV = 'INTV'


parser = argparse.ArgumentParser()

parser.add_argument("-c", "--company", default="", action="store", type=str,
                    required=True, help="the name/ticker of the company you're applying to", nargs=1)
parser.add_argument("-s", "--status", action="store_true",
                    help="get the status of your application to the given company")
parser.add_argument("-i", "--insert", choices=[appStatus.NOAPP, appStatus.APP,
                                                appStatus.REJ, appStatus.MORE,
                                                appStatus.INTV], action="store",
                    help="changes the status of your application to the given status")
args = parser.parse_args()

with open('ReferenceData/tracker.json', 'r') as f:
    data = json.load(f)

givenCompany = args.company[0]

targetCompany = ''

# Searches for the given company
for d in data:
    if (d['Symbol'] == givenCompany or d['Name'] == givenCompany):
        targetCompany = d

# Prints error message if given company is not found
if (targetCompany == ''):
    msg = "Company not found in list of S&P 500 companies"
    print(msg)
    sys.exit(0)

# Gets the status of my application to a company
def getStatus():
    return targetCompany['Status']

# if requested, runs and prints output of getStatus()
if (args.status == True):
    print(getStatus())

# changes the status of my application to a given status
def changeStatus():
    if (targetCompany['Status'] != args.insert):
        targetCompany['Status'] = args.insert
        print('Status successfully changed to: ' + getStatus())
    else:
        print("Application status is already: " + args.insert)

# Calls changeStatus if insert argument is given
if (args.insert != None):
    changeStatus()

# Writes to tracker JSON file
with open('ReferenceData/tracker.json', 'w') as json_file:
    json.dump(data, json_file)
