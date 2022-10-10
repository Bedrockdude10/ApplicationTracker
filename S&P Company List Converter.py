from enum import Enum
import json

# Enum to represent the status of an application
class appStatus(str, Enum):
    NOAPP = 'NOAPP'
    APP = 'APP'
    REJ = 'REJ'
    MORE = 'MORE'
    INTV = 'INTV'

# Open JSON file
with open('ReferenceData/CompanyList.json', 'r') as f:
    data = json.load(f)

# Adds app status to each company in the JSON
for d in data:
    d['Status'] = json.dumps(appStatus.NOAPP)

# Writes to tracker JSON file
with open('ReferenceData/tracker.json', 'w') as json_file:
   json.dump(data, json_file)
