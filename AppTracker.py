#!/usr/bin/env python3
import argparse
import csv
import enum

# Enum to represent the status of an application
class appStatus(enum.Enum):
    noApp = "have not applied"
    app = "application submitted"
    rej = "application rejected"
    more = "more info requested (not an interview)"
    intV = "interview requested"


parser = argparse.ArgumentParser()

parser.add_argument("-c", "--company", default="", action="store", type=str,
                    required=True, help="the name/ticker of the company you're applying to", nargs=1)
parser.add_argument("-s", "--status", action="store_true",
                    help="get the status of your application to the given company")
parser.add_argument("-i", "--insert", choices=[appStatus.noApp.name, appStatus.app.name,
                                                appStatus.rej.name, appStatus.more.name,
                                                appStatus.intV.name],
                    help="changes the status of your application to the given status")
args = parser.parse_args()

given_company = args.company[0]

companies = []

# Reads a CSV file and creates a list of the companies in the S&P 500 and their tickers
with open("ReferenceData/constituents_csv.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        companies.append(row)

# adds the status noApp to the list of companies
for list in companies:
    list.append(appStatus.noApp)

# finds the given company in the list of S&P 500 companies
def findCompany():
    for list in companies:
        if (given_company == list[0] or given_company == list[1]):
            return list
        else:
            msg = "Company not found in list of S&P 500 companies"
            return msg

target_Company = findCompany()

# gets the status of my application to a company
def getStatus():
    return appStatus(target_Company[3]).value

# if requested, runs and prints output of getStatus()
if (args.status == True):
    print(getStatus())

# changes the status of my application to a given status
def changeStatus():
    target_Company[3] = appStatus(args.insert)
    print(getStatus())
