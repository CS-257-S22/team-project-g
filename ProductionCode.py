import sys
import csv
import os
import datetime

relativeDataPath = "Data/dummy_data.csv" #data path of the dataset .csv file relative to this folder
dataSet = [] #2-d array data set in the format [Date (as a tuple of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]

def retrieveData():
    absoluteDataPath = convertRealtivePathToAbsolutePath()
    stringLines = getStringLinesFromFile(absoluteDataPath)
    storeData(stringLines)

def convertRealtivePathToAbsolutePath():
    currentPath = os.path.dirname(__file__)
    return os.path.join(currentPath, relativeDataPath)

def getStringLinesFromFile(filePath):
    with open(filePath) as file:
        stringLines  = file.readlines()[1:]
    file.close()
    return stringLines

def storeData(stringLines):
    for i in stringLines:
        arrayLine = convertStringLinetoArray(i)
        arrayLine.pop() # remove last column
        arrayLine[0] = splitDate(arrayLine[0]) #process date String and make it a duplet
        dataSet.append(arrayLine)

def convertStringLinetoArray(stringLine):
    arrayLine = []
    for i in stringLine.split(","):
        arrayLine.append(i)
    return arrayLine

#Split date in to a tuple (Year, Month, Day)
def splitDate(dateString):
    return dateString.split("-")

# TO print the date in which a specific state had the highest reported cases. 
# To do this, we iterate through the data, looking at the reported cases each day for the specified state. 
# We would start with 0, and update a ‘highestDay’ variable if while iterating through there is a day with higher cases than our count.
def getDayWithMostCases(stateName):
    # first check if stateName is in dataSet
    if stateInData(stateName):
        highestDayCaseCount = 0
        highestDay = "2020-1-1"
        for element in dataSet:
            if (element[2] == stateName):
                if (int(element[3]) > int(highestDayCaseCount)):
                    highestDay = element[0]
                    highestDayCaseCount = element[3]
        print("On " + dayListToStr(highestDay) +" in " + stateName + " there were " + highestDayCaseCount + " cases." )


# Takes list containing date ['year','month','day'] and returns string in form 'Month Day, Year'
def dayListToStr(date):
    datetime_object = datetime.datetime.strptime(date[1], "%m")
    return datetime_object.strftime("%B") + " " + date[2] + ", " + date[0]



        

# returns true if state specified is in dataSet, false otherwise
def stateInData(stateName): 
    for element in dataSet:
        if (element[2] == stateName):
            return True
    print("stateName was not found in dataSet")
    return False


if __name__ == "__main__":
    retrieveData()
    print(dataSet)
    getDayWithMostCases("Minnesota")