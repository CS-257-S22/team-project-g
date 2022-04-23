def checkValidDate(dateString):
    '''
    input: date in String form
    output: a list of 3 Strings, [Year, Month, Date] if the date is formatted correctly
            False if the date is formatted incorrectly
    '''
    try:
        dates = dateString.split("-")
    except: 
        return False
    
    try:
        year = int(dates[0])
        month = int(dates[1])
        day = int(dates[2])
    except:
        return False
    if(year < 2018):
        return False
    if(year > 2022):
        return False
    if(month > 12):
        return False
    if(month < 1):
        return False
    if(day > 31):
        return False
    if(day < 1):
        return False
    return dates