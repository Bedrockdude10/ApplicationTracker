#!/usr/bin/env python3
import argparse
import csv
import enum
import sys

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
                                                appStatus.intV.name], action="store",
                    help="changes the status of your application to the given status")
args = parser.parse_args()

givenCompany = []

companies = []

# Reads a CSV file and creates a list of the companies in the S&P 500 and their tickers
with open("ReferenceData/constituents_csv.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        companies.append(row)

testV = args.company[0]
testV2 =

# adds the status noApp to the list of companies and finds the given
# company in the list of S&P 500 companies
for company in companies:
    if (args.company[0] == company[0] or args.company[0] == company[1]):
        givenCompany = company
    company.append(appStatus.noApp)

# checks if the given company was found
if (givenCompany == []):
    msg = "Company not found in list of S&P 500 companies"
    print(msg)
    sys.exit(0)

# gets the status of my application to a company
def getStatus():
    return appStatus(givenCompany[3]).value

# if requested, runs and prints output of getStatus()
if (args.status == True):
    print(getStatus())


# changes the status of my application to a given status
def changeStatus():
    if (givenCompany[3] != appStatus[args.insert]):
        givenCompany[3] = appStatus[args.insert]
        print(getStatus())
    else:
        print("status is already: ")

if (args.insert != []):
    changeStatus()

with open("ReferenceData/constituents_csv.csv", "w") as file:
    csvwriter = csv.writer(file)

    csvwriter.writerow(companies[0])
    for company in companies:
        if (company[0] == "Symbol"):
            print("symbol row")
        else:
            csvwriter.writerows(company)
