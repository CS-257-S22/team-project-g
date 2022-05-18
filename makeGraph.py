#Makes graph(s) based on a location and dateRange
import helperMakeGraph as hMG
import matplotlib.pyplot as plt
import io
from helperMakeGraph import *
from helperClasses import *
from retrieveData import getDataCombination

def makeGraph(location,dateRange):
    """
    Displays 2 graphs according to a location and a date Range

    inputs:
    locations is a Location object
    dateRange is a DateRange object
    """
    dataCombination = getDataCombination(location,dateRange)
    makeConfirmedCasesGraph(dataCombination.dates,dataCombination.confirmedcases,location)
    plt.show()
    plt.close()
    makeConfirmedCasesGraph(dataCombination.dates,dataCombination.confirmeddeaths,location)
    plt.show()
    plt.close()
    
def makeSeperateGraphs(location,dateRange):
    """
    Stores 2 speperated graphs according to a location and a date Range to an output
    
    inputs:
    locations is a Location object
    dateRange is a DateRange object

    output (): a list that saves the information for 2 graphs [graph1, graph2]
    """
    dataCombination = getDataCombination(location,dateRange)
    makeConfirmedCasesGraph(dataCombination.dates,dataCombination.confirmedcases,location)
    outputConfirmedCases = io.BytesIO()
    outputConfirmedDeaths = io.BytesIO()
    plt.savefig(outputConfirmedCases,format="png")
    plt.close()
    makeConfirmedCasesGraph(dataCombination.dates,dataCombination.confirmeddeaths,location)
    plt.savefig(outputConfirmedDeaths,format="png")
    plt.close()
    return [outputConfirmedCases, outputConfirmedDeaths]
    
       
def makeConfirmedCasesGraph(dates, caseList, location):
    """
    makes a confirmed case graph
    
    inputs:
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    locations is a Location object
    """
    
    drawGraph(dates,caseList)
    labelConfirmedCasesToDate()
    makeTitleConfirmedCases(location.county, location.state)
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)

def makeConfirmedDeathsGraph(dates, caseList, location):
    """
    makes a confirmed deaths graph
    
    inputs:
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    locations is a Location object
    """
    drawGraph(dates,caseList)
    labelConfirmedDeathsToDate()
    makeTitleConfirmedDeaths(location.county, location.state)
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)