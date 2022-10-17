#!/usr/bin/env python3
import pickle
from CustomClasses import Company

# Open pickle file
with open('ReferenceData/tracker.pickle', 'rb') as f:
    data = pickle.load(f)



# Close pickle file
with open('ReferenceData/tracker.pickle', 'wb') as outfile:
    pickle.dump(CompanyList, outfile, protocol=pickle.HIGHEST_PROTOCOL)
