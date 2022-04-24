from datetime import datetime
def toDateTime(date):
    '''convert date [Year, Month, Day] to a datetime object'''
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def splitDate(dateString):
    '''Split date in to a list [Year, Month, Day]'''
    dates = dateString.split("-")
    return dates
