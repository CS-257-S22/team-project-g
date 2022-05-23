#helper functions that supports makeGraph.py, inclusing  calculating and setting ticks
#making labels and titles, formatting and drawing graph
from retrieveData import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import math
from matplotlib.figure import Figure
from datetime import datetime
from helperClasses import DataCombination

#functions related to setting x axis ticks
def setXaxisTicks(timeRangeDays):
    """set tick size and format on x axis"""
    setXaxisLocator(timeRangeDays)
    setXAxisFormat()
    
def setXaxisLocator(timeRangeDays):
    """depending on the range of time that is displayed on the graph, set the tick size on x axis"""
    if(timeRangeDays < 90): 
        #range is within 3 months: set ticks by day, make total number of ticks close to 10 (1 - 20)
        setDayLocator(max(1, int(timeRangeDays/10)))
    else:
        #range is greater than 3 months: set ticks by month, make total number of ticks close to 10 (1 - 20)
        timeRangeMonth = timeRangeDays/30
        setMonthLocator(max(1, int(timeRangeMonth/10)))
        
def setDayLocator(interval):
    """
    set x axis locator, each tick per interval days
    input: interval, an integer corresponding to the size of the ticks on the x axis
    """
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = interval))
    
def setMonthLocator(interval):
    """
    set x axis locator, each tick per interval months
    input: interval, an integer corresponding to the size of the ticks on the x axis
    """
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = interval))

def setXAxisFormat():
    """set the format of display on x axis"""
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gcf().autofmt_xdate()
    
#functions related to setting Y axis ticks
def calculateYTickSize(caseList):
    """
    takes in a  list of case number and return the appropriate tick size for it
    input: a list of case number, in int
    """
    diffCases = int(caseList[-1]) - int(caseList[0])
    #Avoid futher math if there are no cases in the interval
    if (diffCases == 0):
        return caseList[0]
    yticksize = int(math.log10(diffCases)) 
    
    #Find the least power of 10 that is less than max cases and make it the tick size
    yticksize = int(math.pow(10,yticksize))
    
    #If the max number of cases is 1----, then make the tick size 1/10 its original
    if int (diffCases/yticksize) == 1: 
        yticksize/=10
        
    #If the tick size is less than 1, make it 1
    yticksize = max(yticksize, 1)   
    return int(yticksize)

def setYaxisTicks(yticksize):
    """
    set tick size on y axis to yticksize
    input: yticksize, an integer corresponding to the size of the ticks on the y axis
    """
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base = yticksize))
    
#fucntions related to labeling and titling
def makeTitleConfirmedCases(county, state): 
    """make title for confirmed cases graph according to the county name and state name""" 
    plt.title("Cumulative Number of Confirmed Cases in " + county + "," + state)
    
def makeTitleConfirmedDeaths(county, state): 
    """make title for confirmed deaths graph according to the county name and state name""" 
    plt.title("Cumulative Number of Confirmed Deaths in " + county + "," + state)

def labelConfirmedCasesToDate():
    """make label for confirmed cases graph""" 
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    
def labelConfirmedDeathsToDate():
    """make label for confirmed deaths graph""" 
    plt.xlabel("Date")
    plt.ylabel("Confirmed Deaths")

#functiosn related to graphing
def drawGraph(dates,caseList): 
    """
    draw an unformatted graph of caseList to dates
    case
    """
    xpoints = toDatetimeList(dates)
    ypoints = caseList
    plt.plot(xpoints, ypoints)

#datetime conversion    
def toDatetimeList(dates):
    """
    converts the dates list to datetime object list
    input: dates, a list with elements of format ['YYYY','MM', 'DD']
    """
    datetimes = []
    for i in dates:
        tmpdatetime = toDateTime(i)
        datetimes.append(tmpdatetime)
    return datetimes

def getTimeRangeDays(dates):
    """
    return the time range covered by data
    input: dates, a list with elements of format ['YYYY','MM', 'DD']
    """
    startDate = toDateTime(dates[0])
    endDate = toDateTime(dates[-1])
    deltatime = endDate - startDate
    return deltatime.days
