from enum import Enum
import datetime

# Enum to represent the status of an application
class appStatus(str, Enum):
    NOAPP = 'NOAPP'
    APP = 'APP'
    REJ = 'REJ'
    MORE = 'MORE'
    INTV = 'INTV'

# Class to represent a company
class Company:
    def __init__(self, name, sector, symbol, snP):
        self.Name = name
        self.Sector = sector
        self.Symbol = symbol
        self.SnP = snP
        self.Apps = set()

# Class to represent an application to a company
# Coop is true if applied for a co-op; false for internship
# Cyber is true if potential for a cybersecurity role; false for straight CS
class Application:
    def __init__(self, companySymbol, position, coop, cyber, date):
        self.CompanySymbol = companySymbol
        self.Position = position;
        self.Coop = coop;
        self.Cyber = cyber;
        self.Status = appStatus.APP
        self.Date = date;
