from enum import Enum

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

    # Override default equals function
    def __eq__(self, other):
        if isinstance(other, Company):
            names = self.Name == other.Name
            sectors = self.Sector == other.Sector
            symbols = self.Symbol == other.Symbol
            snP = self.SnP == other.SnP
            if names and sectors and symbols and snP:
                return True
        return False

    # Override default hash function
    def __hash__(self):
        return hash(self.Name) + hash(self.Sector) + hash(self.Symbol) + hash(self.SnP)

# Enum to represent the medium used to apply to a company
class AppMedium(str, Enum):
    Linkedin = 'Linkedin'
    NUWorks = 'NUWorks'
    Website = 'Company website'

# Function to parse the argument for application medium
# Returns null if unable to parse given medium
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

    # Override default equals function
    def __eq__(self, other):
        if isinstance(other, Application):
            positions = self.Position == other.Position
            companies = self.CompanySymbol == other.CompanySymbol
            coops = self.Coop == other.Coop
            cybers = self.Cyber == other.Cyber
            mediums = self.Medium == other.Medium
            if positions and companies and coops and cybers and mediums:
                return True
        return False

    # Override default hash function
    def __hash__(self):
        return hash(self.Position) + hash(self.CompanySymbol) + hash(self.Coop)
