#!/usr/bin/env python3
import pickle
import json
from CustomClasses import Company

# Open JSON file
with open('ReferenceData/CompanyList.json', 'r') as f:
    data = json.load(f)

# New list of companies
CompanyList = {}

# For every dictionary imported from the JSON, create a corresponding Company object
for dictionary in data:
    c = Company(dictionary['Name'], dictionary['Sector'], dictionary['Symbol'], True)
    CompanyList[c.Symbol] = c

with open('ReferenceData/tracker.pickle', 'wb') as outfile:
    pickle.dump(CompanyList, outfile, protocol=pickle.HIGHEST_PROTOCOL)
