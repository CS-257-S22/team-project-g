#gets data from our online database for our functions
import psycopg2
import psqlConfig as config

from CoreFunctions.conversionFunctions import *
from CoreFunctions.indexDictionary import *
from CoreFunctions.helperClasses import *

'''
def getDataCombination(location, dateRange):

    dataSet = getDataWithLocationAndDateRange(location, dateRange)
    dates = getDates(dataSet)
    confirmedCases = getConfirmedCases(dataSet)
    confirmedDeaths = getConfirmedDeaths(dataSet)
    return DataCombination(dates, confirmedCases, confirmedDeaths)
'''

def getDataCombination(location, dateRange):
    """
    Inputs: 
    locations is a Location object
    dateRange is a DateRange object

    Output:
    returns a DataCombanation object for graphing and displaying raw data
    """
    my_source = DataSource()
    rawdata = my_source.queryForDataCombination(location, dateRange)
    dataCombination = processData(rawdata)
    return dataCombination

def processData(rawData):
    """
    processes the raw data obtained from the database to make a DataCombination object

    input: rawData, a list of tuples (date, confirmedCases, confirmedDeaths)
    in which date is a datetime object; confirmedCases and confirmedDeaths are integers

    output: a DataCombination object
    """ 

    dates = [datetimetoList(i[0]) for i in rawData]
    confirmedCases = [i[1] for i in rawData]
    confirmedDeaths = [i[2] for i in rawData]
    return DataCombination(dates, confirmedCases, confirmedDeaths)

class DataSource:
    '''this is the object that connects the database to python code'''
    def __init__(self):
        '''this intlizes the variable that points to the database'''
        self.connection = self.connect()

    def connect(self):
        '''this opens the connection to the pesfied data base or returns an error if the data base cannot be reached'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def queryForDataCombination(self,location, dateRange):
        '''
        get data according to county and state in the database
        input: countyName, stateName as strings
        output: a tuple object of data
        '''
        stateName = location.state
        countyName = location.county
        datetimeStartDate = toDateTime(dateRange.startDate)
        datetimeEndDate = toDateTime(dateRange.endDate)
        try:
            cursor = self.connection.cursor()
            query = "SELECT Date, ConfirmedCases, ConfirmedDeaths FROM  CovidData WHERE StateName = %s AND CountyName =%s AND Date >= %s AND Date <= %s"
            cursor.execute(query, (stateName, countyName, datetimeStartDate, datetimeEndDate))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None