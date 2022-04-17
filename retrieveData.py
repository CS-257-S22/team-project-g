import sys
import csv
import os
 #data path of the dataset .csv file relative to this folder
dataSet = [] #2-d array data set in the format [Date (as a tuple of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]

def retrieveData(relativeDataPath):
    absoluteDataPath = convertRealtivePathToAbsolutePath(relativeDataPath)
    stringLines = getStringLinesFromFile(absoluteDataPath)
    storeData(stringLines)
    return dataSet

def convertRealtivePathToAbsolutePath(relativeDataPath):
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
        arrayLine[0] = splitDate(arrayLine[0]) #process date String and make it a list
        arrayLine[3] = int (arrayLine[3])
        arrayLine[4] = int (arrayLine[4])
        dataSet.append(arrayLine)

def convertStringLinetoArray(stringLine):
    arrayLine = []
    for i in stringLine.split(","):
        arrayLine.append(i)
    return arrayLine

#Split date in to a list [Year, Month, Day]
def splitDate(dateString):
    return dateString.split("-")