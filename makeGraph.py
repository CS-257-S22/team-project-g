# 
# This code is not a part of the Command Line project.
# points to improve: 
#   1. low effciency overall; maybe we have to use a smpling method
#   2. the death number is not cumulative, but the confirmed cases seem to be cumulative
import helperMakeGraph as hMG
import matplotlib.pyplot as plt
from helperMakeGraph import *

def makeGraph(location,dateRange):
    info = hMG.getDataForGraph(location,dateRange)
    if(info == False): 
        print("Data not Found!")
        return "Data not Found!"
    makeConfirmedCasesGraph(info[0],info[1],location)
    plt.show()
    plt.close()
    makeConfirmedDeathsGraph(info[0],info[2],location)
    plt.show()
    plt.close()

def make2GraphToOutPut(location,dateRange,output):
    plt.close()
    plt.rcParams["figure.figsize"] = (15,4)
    
    info = hMG.getDataForGraph(location,dateRange)
    if(info == False): 
        print("Data not Found!")
        return "Data not Found!"
    
    plt.subplot(121)
    makeConfirmedCasesGraph(info[0],info[1],location)
    plt.subplot(122)
    makeConfirmedDeathsGraph(info[0],info[2],location)
    plt.tight_layout()
    plt.savefig(output,format="png")
    plt.close()
    return True
       
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

if __name__ == '__main__':
    location = ["Rice", "Minnesota"]
    dateRange = [['2020', '2', '1'] , ['2021', '10', '1']]
    makeGraph(location,dateRange)
    