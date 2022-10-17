from enum import Enum
import datetime

# Enum to represent the status of an application
class AppStatus(str, Enum):
    NOAPP = 'NOAPP'
    APP = 'APP'
    REJ = 'REJ'
    MORE = 'MORE'
    INTV = 'INTV'

# Enum to represent the sector of a given company
class SectorType(str, Enum):
    Energy = 'Energy'
    Materials = 'Materials'
    Industrials = 'Industrials'
    Utilities = 'Utilities'
    Healthcare = 'Healthcare'
    Financials = 'Financials'
    Misc = 'Consumer Discretionary'
    Staples = 'Consumer Staples'
    Info = 'Information Technology'
    Communication = 'Communication Services'
    Real = 'Real Estate'

# Class to represent a company
class Company:
    def __init__(self, name, sector, symbol, snP):
        self.Name = name
        # check that given sector is one of the defined sectors
        if not isinstance(sector, SectorType):
            print('Sector must be a SectorType')
            return
        self.Sector = sector
        # check that symbol is not a string > 5 in length
        if len(symbol) > 5:
            print('Symbol must be 5 characters or less')
            return
        self.Symbol = symbol
        # check that snP is a boolean
        if not isinstance(snP, bool):
            print('snP status must be a boolean')
            return
        self.SnP = snP
        self.Apps = set()

# Enum to represent the medium used to apply to a company
class AppMedium(str, Enum):
    Linkedin = 'Linkedin'
    NUWorks = 'NUWorks'
    Website = 'Company website'

# Class to represent an application to a company
# Coop is true if applied for a co-op; false for internship
# Cyber is true if potential for a cybersecurity role; false for straight CS
# Medium is the way you applied, i.e. NUWorks, Linkedin, website, etc.
class Application:
    def __init__(self, companySymbol, position, coop, cyber, date, medium):
        self.CompanySymbol = companySymbol
        self.Position = position
        if not isinstance(coop, bool):
            print('coop status must be a boolean')
            return
        self.Coop = coop
        if not isinstance(cyber, bool):
            print('cyber status must be a boolean')
            return
        self.Cyber = cyber
        self.Status = AppStatus.APP
        self.Date = date
        if not isinstance(medium, AppMedium):
            print('Medium must be a valid medium')
            return
        self.Medium = medium
