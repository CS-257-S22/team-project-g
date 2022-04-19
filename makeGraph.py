# 
# This code is not a part of the Command Line project.
# points to improve: 
#   1. low effciency overall; maybe we have to use a smpling method
#   2. the death number is not cumulative, but the confirmed cases seem to be cumulative
import helperMakeGraph as hMG
import retrieveData as rD
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import math
from datetime import datetime

def makeGraph(location,dateRange):
    list = hMG.getDataWithLocationAndDateRange(location, dateRange)
    dates = hMG.getDates(list)
    confirmedCases = hMG.getConfirmedCases(list)
    confirmedDeaths = hMG.getConfirmedDeaths(list)
    makeConfirmedCasesGraph(dates,confirmedCases,location)
    makeConfirmedDeathsGraph(dates,confirmedDeaths,location)
    
def makeConfirmedCasesGraph(dates, caseList, location):
    '''
    makes a confirmed case graph
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    Location is a list of 2, [county, state]
    '''
    
    drawGraph(dates,caseList)
    labelConfirmedCasesToDate()
    makeTitleConfirmedCases(location[0], location[1])
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)
    
    plt.show()
    plt.close() 
def makeConfirmedDeathsGraph(dates, caseList, Location):
    '''
    makes a confirmed deaths graph
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    Location is a list of 2, [county, state]
    '''
    drawGraph(dates,caseList)
    labelConfirmedDeathsToDate()
    makeTitleConfirmedDeaths(Location[0], Location[1])
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)
    
    plt.show()
    plt.close() 

#functions related to setting x axis ticks
def setXaxisTicks(timeRangeDays):
    '''set tick size and format on x axis'''
    setXaxisLocator(timeRangeDays)
    setXAxisFormat()
    
def setXaxisLocator(timeRangeDays):
    '''depemding on the range of time that is displayed on the graph, set the tick size on x axis'''
    if(timeRangeDays < 90): 
        #range is within 3 months: set ticks by day, make total number of ticks close to 10 (1 - 20)
        setDayLocator(max(1, int(timeRangeDays/10)))
    else:
        #range is greater than 3 months: set ticks by month, make total number of ticks close to 10 (1 - 20)
        timeRangeMonth = timeRangeDays/30
        setMonthLocator(max(1, int(timeRangeMonth/10)))
        
def setDayLocator(intv):
    '''set x axis locator, each tick per intv days'''
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = intv))
    
def setMonthLocator(intv):
    '''set x axis locator, each tick per intv months'''
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = intv))

def setXAxisFormat():
    '''set the format of display on x axis'''
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gcf().autofmt_xdate()
    
#functions related to setting Y axis ticks
def calculateYTickSize(caseList):
    '''takes in a list of case number and return the appropriate tick size for it'''
    maxCases = int(caseList[-1])
    #Avoid futher math if there are no cases in the interval
    if (maxCases == 0):
        return 10
    yticksize = int(math.log10(maxCases)) 
    
    #Find the least power of 10 that is less than max cases and make it the tick size
    yticksize = int(math.pow(10,yticksize))
    
    #If the max number of cases is 1----, then make the tick size 1/10 its original
    if int (maxCases/yticksize) == 1: 
        yticksize/=10
           
    return yticksize

def setYaxisTicks(yticksize):
    '''set tick size on y axis to yticksize'''
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base = yticksize))

#fucntions related to labeling and titling
def makeTitleConfirmedCases(county, state): 
    '''make title for confirmed cases graph''' 
    plt.title("Cumulative Number of Confirmed Cases in " + county + "," + state)
    
def makeTitleConfirmedDeaths(county, state): 
    '''make title for confirmed deaths graph''' 
    plt.title("Non-cumulative Number of Confirmed Deaths in " + county + "," + state)

def labelConfirmedCasesToDate():
    '''make label for confirmed cases graph''' 
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    
def labelConfirmedDeathsToDate():
    '''make label for confirmed deaths graph''' 
    plt.xlabel("Date")
    plt.ylabel("Confirmed Deaths")

#functiosn related to graphing
def drawGraph(dates,caseList): 
    '''draw an unformatted graph of caseList to dates'''
    xpoints = toDatetimeList(dates)
    ypoints = caseList
    plt.plot(xpoints, ypoints)

#datetime conversion    
def toDatetimeList(dates):
    '''converts the dates list to datetime object list'''
    datetimes = []
    for i in dates:
        tmpdatetime = datetime(int(i[0]),int(i[1]),int(i[2]))
        datetimes.append(tmpdatetime)
    return datetimes

def getTimeRangeDays(dates):
    '''return the time range covered by data'''
    startDate = dates[0]
    startDate = datetime(int(startDate[0]),int(startDate[1]),int(startDate[2]))
    endDate = dates[-1]
    endDate = datetime(int(endDate[0]),int(endDate[1]),int(endDate[2]))
    deltatime = endDate - startDate
    return deltatime.days

if __name__ == '__main__':
    location = ["Autauga", "Alabama"]
    dateRange = [['2020', '1', '1'] , ['2020', '12', '1']]
    makeGraph(location,dateRange)