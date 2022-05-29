#some helper functions for converting from one type to another
from datetime import datetime

def toDateTime(date):
    """convert date [Year, Month, Day] in string to a datetime object"""
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def datetimetoList(date):
    """convert  a datetime object to a date list whose element are in string [Year, Month, Day]"""
    return [str(date.year), str(date.month), str(date.day)]
    
def splitDate(dateString):
    """Split date in to a list [Year, Month, Day]"""
    dates = dateString.split("-")
    return dates