from dataclasses import dataclass
from datetime import datetime

@dataclass
class CashFlow:
    """
    A class used to represent the Cash Flow of a company

    ...

    Attributes
    ----------
    unique_id : str
        unique identifier for each instance
    date : datetime
        the date of the cash flow
    symbol : str
        the stock symbol of the company
    cik : str
        the Central Index Key (CIK) of the company
    reported_currency : str
        the currency in which the cash flow is reported
    filling_date : datetime
        the date when the cash flow was filled
    accepted_date : datetime
        the date when the cash flow was accepted
    calendar_year : int
        the year of the calendar
    period : str
        the financial period
    link : str
        the link to the cash flow document
    final_link : str
        the final link to the cash flow document
    operating_activities : OperatingActivities
        instance of OperatingActivities class
    investing_activities : InvestingActivities
        instance of InvestingActivities class
    financing_activities : FinancingActivities
        instance of FinancingActivities class
    cash_position : CashPosition
        instance of CashPosition class
    supplemental_data : SupplementalData
        instance of SupplementalData class
    """

    unique_id: str
    date: datetime
    symbol: str
    cik: str
    reported_currency: str
    filling_date: datetime
    accepted_date: datetime
    calendar_year: int
    period: str
    link: str
    final_link: str

    operating_activities: OperatingActivities = None
    investing_activities: InvestingActivities = None
    financing_activities: FinancingActivities = None
    cash_position: CashPosition = None
    supplemental_data: SupplementalData = None
