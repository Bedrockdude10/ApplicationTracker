#!/usr/bin/env python3
import pickle
import json
from CustomClasses import Company, SectorType

# Function to map the given argument for sector to its SectorType enum
#     Energy = 'Energy'
#     Materials = 'Materials'
#     Industrials = 'Industrials'
#     Utilities = 'Utilities'
#     Healthcare = 'Healthcare'
#     Financials = 'Financials'
#     Misc = 'Consumer Discretionary'
#     Staples = 'Consumer Staples'
#     Info = 'Information Technology'
#     Communication = 'Communication Services'
#     Real = 'Real Estate'
def parseSector(given):
    match given:
        case 'Energy':
            return SectorType.Energy
        case 'Materials':
            return SectorType.Materials
        case 'Industrials':
            return SectorType.Industrials
        case 'Utilities':
            return SectorType.Utilities
        case 'Healthcare':
            return SectorType.Healthcare
        case 'Health Care':
            return SectorType.Healthcare
        case 'Financials':
            return SectorType.Financials
        case 'Misc':
            return SectorType.Misc
        case 'Consumer Discretionary':
            return SectorType.Misc
        case 'Staples':
            return SectorType.Staples
        case 'Consumer Staples':
            return SectorType.Staples
        case 'Info':
            return SectorType.Info
        case 'Information Technology':
            return SectorType.Info
        case 'Communication':
            return SectorType.Communication
        case 'Communication Services':
            return SectorType.Communication
        case 'Real':
            return SectorType.Real
        case 'Real Estate':
            return SectorType.Real
        case default:
            print('Unable to parse sector')
            return None

# Open JSON file
with open('ReferenceData/CompanyList.json', 'r') as f:
    data = json.load(f)

# New list of companies
CompanyList = {}

# For every dictionary imported from the JSON, create a corresponding Company object
for dictionary in data:
    c = Company(dictionary['Name'], parseSector(dictionary['Sector']), dictionary['Symbol'], True)
    CompanyList[c.Symbol] = c

with open('ReferenceData/tracker.pickle', 'wb') as outfile:
    pickle.dump(CompanyList, outfile, protocol=pickle.HIGHEST_PROTOCOL)
