import sys
import csv
import os

dataSet = []

def retrieveData(filePath):
    with open(filePath) as file:
        lines = file.readlines()[1:]
    lines = lines
    for i in lines:
        line = []
        for j in i.split(","):
            line.append(j)
        line.pop()
        dataSet.append(line)
    file.close()

def convertRealtivePathtoAbsolutePath(relativePath):
    currentPath = os.path.dirname(__file__)
    return os.path.join(currentPath, relativePath)

def callRetrieveData():
    relativeDataPath = "Data/dummy_data.csv"
    absoluteDataPath = convertRealtivePathtoAbsolutePath(relativeDataPath)
    retrieveData(absoluteDataPath)

if __name__ == "__main__":
    callRetrieveData()
    print(dataSet[0][0])
    