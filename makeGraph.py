# makes a graph out of a dates[] list and a Cases[] list;
# points to improve: the pd.to_datetime() takes a string rather than a list, 
# so the convertDateListtoDateString(dateList) could be saved 
# low effciency overall; maybe we have to use a smpling method
 
import pandas as pd
import retrieveData as rD
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import numpy as np
from datetime import datetime


#dates[] list contains lists of date in the format [Year, Month, Day]
#confirmedCases[] list contains number of cases
def makeConfirmedCasesGraph(dates, caseList):

    dates = toDatetimeList(dates)

    xpoints = dates
    ypoints = caseList

    labelDateToConfirmedCases()
    maxCases = int(caseList[-1])
    maxCases = maxCases * 1.05
    
    yticksize = int(math.log10(maxCases))
    yticksize = math.pow(10,yticksize-1)

    plt.yticks(np.arange(0,maxCases,yticksize))
    axes = plt.axes()
    plt.title("Change in Cases to Date Graph")

    plt.plot(xpoints, ypoints)
    plt.show()

#converts the dates list to datetime objects
def toDatetimeList(dates):
    datetimes = []
    for i in dates:
        tmpdatetime = datetime(int(i[0]),int(i[1]),int(i[2]))
        datetimes.append(tmpdatetime)
    return datetimes

def labelDateToConfirmedCases():
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")

def labelDateToConfirmedDeaths():
    plt.xlabel("Date")
    plt.ylabel("Confirmed Deaths")

if __name__ == "__main__":
    plotTestDataRelativePath = "Data/plot_test_data.csv"
    plotTestDataSet = rD.retrieveData(plotTestDataRelativePath)
    dates = [i[0] for i in plotTestDataSet]
    cases = [i[3] for i in plotTestDataSet]
    makeConfirmedCasesGraph(dates,cases)