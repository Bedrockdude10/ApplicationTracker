#!/usr/bin/env python3
import argparse
import datetime

from CustomClasses import SectorType
from CompanyListConverter import parseSector
from CustomClasses import Application, AppMedium, Company
import pickle
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--company", default="", action="store", type=str, required=True,
                    help="the ticker of the company you're applying to")
parser.add_argument("-i", "--insert", nargs=4,
                    help="adds a new company. order: name, sector, symbol, snP")
parser.add_argument("-a", "--apply", nargs=4,
                    help="adds an application. order: position, coop, cyber, medium")
parser.add_argument("-u", "--unapply", nargs=3,
                    help="removes an application. order: position, coop, cyber")
parser.add_argument("-r", "--remove", nargs=4,
                    help="removes a company from the company list")
args = parser.parse_args()

# Open pickle file
with open('ReferenceData/tracker.pickle', 'rb') as f:
    data = pickle.load(f)

# Checks that we are not adding a new company to the list
if args.insert == None:
    # Searches for the given company and exits if not found
    if args.company not in data:
        print('Requested company key not found in company list')
        sys.exit()
    else:
        targetCompany = data[args.company]
        apps = targetCompany.Apps
        if apps == set():
            print('No applications submitted to: ' + targetCompany.Symbol)
        else:
            for app in apps:
                print(app.Position + ' ' + str(app.Date) + ' ' + app.Status)

# Function to add a company to the list
def addCompany(name, sector, symbol, snP):
    if parseSector(sector) == None:
        return
    if (data.has_key(symbol)):
        print('Company already exists in list')
        return
    try:
        newCompany = Company(name, parseSector(sector), symbol, snP)
        data[symbol] = newCompany
        print('Successfully added: ' + newCompany.Symbol)
    except:
        print('Unable to add company to list')
        return

# Function to remove a company from the list
def removeCompany(symbol):
    if (not (data.has_key(symbol))):
        print('Company does not exist in list')
        return
    try:
        removed = data.pop(symbol)
        print('Successfully removed: ' + removed.Symbol)
    except:
        print('Unable to remove company from list')

# Function to add an application to the company
def addApp(symbol, position, coop, cyber, date, medium):
    if medium == None:
        print('Medium cannot be null')
        return
    newApp = Application(symbol, position, coop, cyber, date, medium)
    if (newApp in targetCompany.Apps):
        print('Application already exists at this company')
        return
    try:
        targetCompany.Apps.add(newApp)
        print('Successfully added: ' + newApp.CompanySymbol + ' ' + newApp.Position)
    except:
        print('Unable to add application to company')

# Function to remove an application from a company
def removeApp(symbol, position, coop, cyber, date):
    toBeRemoved = Application(symbol, position, coop, cyber, date)
    if toBeRemoved not in targetCompany.Apps:
        print('Application does not exist at this company')
        return
    try:
        targetCompany.Apps.remove(toBeRemoved)
        print('Successfully removed: ' + toBeRemoved.CompanySymbol + toBeRemoved.Position)
    except:
        print('Unable to remove application from company')

# Function to parse the argument for application medium
def parseMedium(given):
    match given:
        case 'L': return AppMedium.Linkedin
        case 'LinkedIn': return AppMedium.Linkedin
        case 'Linkedin': return AppMedium.Linkedin
        case 'W': return AppMedium.Website
        case 'Website': return AppMedium.Website
        case 'N': return AppMedium.NUWorks
        case 'NUWorks': return AppMedium.NUWorks
        case default:
            print('Unable to parse medium')
            return None

# Add given company if a new company is given
if args.insert != None:
    name = args.insert[0]
    sector = args.insert[1]
    symbol = args.insert[2]
    snP = args.insert[3]
    if len(symbol) > 5:
        print('Check given symbol')
    else:
        addCompany(name, sector, symbol, snP)

test = args.apply[1] == 'T'

# Adds an application to given company
if args.apply != None:
    position = args.apply[0]
    coop = False
    cyber = False
    if (args.apply[1] == 'T' or args.apply[1] == 'True'):
        coop = True
    if (args.apply[2] == 'T' or args.apply[2] == 'True'):
        cyber = True
    date = datetime.date.today()
    medium = parseMedium(args.apply[3])

    addApp(targetCompany.Symbol, position, coop, cyber, date, medium)

# Removes an application from given company
if args.unapply != None:
    position = args.apply[0]
    coop = args.apply[1]
    cyber = args.apply[2]
    if (coop == 'T'):
        coop = True
    else:
        coop = False
    if (cyber == 'T'):
        cyber = True
    else:
        cyber = False
    position = args.apply[0]
    coop = args.apply[1]
    cyber = args.apply[2]
    date = datetime.date.today()
    removeApp(targetCompany.Symbol, position, coop, cyber, date)

# Dates/times for version control
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
hour = str(now.hour)
min = str(now.minute)
sec = str(now.second)
mic = str(now.microsecond)
vList = [year, month, day, hour, min, sec, mic]
version = '.'.join(vList)

# Write to versioned pickle file
with open('ReferenceData/Versions/tracker' + version + '.pickle', 'wb') as outf:
    pickle.dump(data, outf, protocol=pickle.HIGHEST_PROTOCOL)

# Close pickle file
with open('ReferenceData/tracker.pickle', 'wb') as outf:
    pickle.dump(data, outf, protocol=pickle.HIGHEST_PROTOCOL)
