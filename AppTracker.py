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

companyDict = {}

# Class to represent a company
class Company:
    def __init__(self, ticker, name, sector):
        self.ticker = ticker;
        self.name = name;
        self.sector = sector;
        self.appStatus = appStatus.noApp;

# Reads a CSV file and creates a list of the companies in the S&P 500 and their tickers
with open("ReferenceData/constituents_csv.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        newCompany = Company(row[0], row[1], row[2])
        companyDict[newCompany.ticker] = newCompany
        print("Company added to companyDict: " + row[0])

# checks if the given company was found
if (args.company[0] == "" or companyDict.get(args.company[0]) == None):
    msg = "Company not found in list of S&P 500 companies"
    print(msg)
    #sys.exit(0)

givenCompany = companyDict.get(args.company[0])

# gets the status of my application to a company
def getStatus():
    return givenCompany.appStatus.value

# if requested, runs and prints output of getStatus()
if (args.status == True):
    print(getStatus())

# changes the status of my application to a given status
def changeStatus():
    if (args.insert != []):
        if (givenCompany.appStatus != appStatus[args.insert]):
            givenCompany.appStatus = appStatus[args.insert]
            print(getStatus())
        else:
            print("status is already: ")

if (args.insert != []):
    changeStatus()

with open("ReferenceData/constituents_csv.csv", "w") as file:
    csvwriter = csv.writer(file)
    # write the first row
    csvwriter.writerow(companyDict["Symbol"])
    # write the rest of the rows
    csvwriter.writerows(zip(*companyDict.values()))
