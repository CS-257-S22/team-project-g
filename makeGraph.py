# makes a graph out of a dates[] list and a cases[] list;
# This code is not a part of the Command Line project.
# points to improve: 
#   1. low effciency overall; maybe we have to use a smpling method
#   2. the death number is not cumulative, but the confirmed cases seem to be cumulative
import pandas as pd
import retrieveData as rD
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import math
import numpy as np
from datetime import datetime


#dates[] list contains lists of date in the format [Year, Month, Day]
#confirmedCases[] list contains number of cases

def makeConfirmedCasesGraph(dates, caseList, Location):
    
    drawGraph(dates,caseList)
    labelConfirmedCasesToDate()
    makeTitleConfirmedCases(Location[0], Location[1])
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)
    
    plt.show()
    
def makeConfirmedDeathsGraph(dates, caseList,Location):
    
    drawGraph(dates,caseList)
    labelConfirmedDeathsToDate()
    makeTitleConfirmedDeaths(Location[0], Location[1])
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)
    
    plt.show()
    
'''functions related to setting x axis ticks'''
def labelConfirmedCasesToDate():
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")

def setXaxisTicks(timeRangeDays):
    setXaxisLocator(timeRangeDays)
    setXAxisFormat()
    
def setXaxisLocator(timeRangeDays):
    if(timeRangeDays < 90): 
        #range is within 3 months: set ticks by day, make total number of ticks close to 10 (1 - 20)
        setDayLocator(max(1, int(timeRangeDays/10)))
    else:
        #range is greater than 3 months: set ticks by month, make total number of ticks close to 10 (1 - 20)
        timeRangeMonth = timeRangeDays/30
        setMonthLocator(max(1, int(timeRangeMonth/10)))
        
def setDayLocator(intv):
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = intv))
    
def setMonthLocator(intv):
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = intv))

def setXAxisFormat():
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gcf().autofmt_xdate()
    
'''functions related to setting Y axis ticks'''
def calculateYTickSize(caseList):
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
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base = yticksize))

'''fucntions related to labeling and titling'''
def makeTitleConfirmedCases(county, state): 
    plt.title("Cumulative Number of Confirmed Cases in " + county + "," + state)
    
def makeTitleConfirmedDeaths(county, state): 
    plt.title("Non-cumulative Number of Confirmed Deaths in " + county + "," + state)
    
def labelConfirmedDeathsToDate():
    plt.xlabel("Date")
    plt.ylabel("Confirmed Deaths")

'''functiosn related to graphing'''
def drawGraph(dates,caseList): 
    xpoints = toDatetimeList(dates)
    ypoints = caseList
    plt.plot(xpoints, ypoints)

'''datetime conversion'''    
#converts the dates list to datetime objects
def toDatetimeList(dates):
    datetimes = []
    for i in dates:
        tmpdatetime = datetime(int(i[0]),int(i[1]),int(i[2]))
        datetimes.append(tmpdatetime)
    return datetimes

#return the time range covered by data
def getTimeRangeDays(dates):
    startDate = dates[0]
    startDate = datetime(int(startDate[0]),int(startDate[1]),int(startDate[2]))
    endDate = dates[-1]
    endDate = datetime(int(endDate[0]),int(endDate[1]),int(endDate[2]))
    deltatime = endDate - startDate
    return deltatime.days

if __name__ == "__main__":
    plotTestDataRelativePath = "Data/plot_test_data.csv"
    plotTestDataSet = rD.retrieveData(plotTestDataRelativePath)
    dates = [i[0] for i in plotTestDataSet]
    cases = [i[4] for i in plotTestDataSet]
    Location = plotTestDataSet[0][1:3]
    makeConfirmedDeathsGraph(dates,cases,Location)