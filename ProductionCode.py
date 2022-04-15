import sys
import csv
import os

dataSet = []

def retrieveData(filePath):
    with open(filePath) as file:
        stringLines  = file.readlines()[1:]
    for i in stringLines:
        arrayLine = convertStringLinetoArray(i)
        dataSet.append(arrayLine)
        arrayLine.pop()
    file.close()

def convertStringLinetoArray(stringLine):
    arrayLine = []
    for i in stringLine.split(","):
        arrayLine.append(i)
    return arrayLine

def convertRealtivePathtoAbsolutePath(relativePath):
    currentPath = os.path.dirname(__file__)
    return os.path.join(currentPath, relativePath)

def callRetrieveData():
    relativeDataPath = "Data/dummy_data.csv"
    absoluteDataPath = convertRealtivePathtoAbsolutePath(relativeDataPath)
    retrieveData(absoluteDataPath)

if __name__ == "__main__":
    callRetrieveData()
    print(dataSet)
    