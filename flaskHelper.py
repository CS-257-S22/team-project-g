import csv
from flask import Flask
import io
import makeGraph as mG
import os
import sys
import base64

location = ["Autauga", "Alabama"]
def checkErrorInput(startDateString, endDateString):
    '''
    Check whether the inputted strings are correctly formatted. 
    Return: True if correctly formatted
            An error message if not
    '''
    startDateList =  checkValidDate(startDateString)
    endDateList = checkValidDate (endDateString)
    if (startDateList == False or endDateList == False):
        msg = "Please enter corret dates! Try .../graph/2020-1-1/2020-12-1"
        return msg
    return True

def getData(startDateList, endDateList):
    '''
    get image data from makeGraph
    
    input: startDateList and endDateList in the format [Year, Month, Date]
    
    output: "Data Not Found!" if no information is found
            image data if the input is correctly formatted and the information is in database
    '''
    dateRange = [startDateList, endDateList]
    output = io.BytesIO()
    
    isData = mG.make2GraphToOutPut(location,dateRange,output)
    if(not(isData)):
        return "Data Not Found!"
    
    data = base64.b64encode(output.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

def checkValidDate(dateString):
    '''
    A copy of checkValidDate() from retrieveData due to error caused by imports
    
    input: date in String form
    output: a list of 3 Strings, [Year, Month, Date] if the date is formatted correctly
            False if the date is formatted incorrectly
    '''
    try:
        dates = dateString.split("-")
    except: 
        return False
    
    try:
        year = int(dates[0])
        month = int(dates[1])
        day = int(dates[2])
    except:
        return False
    if(year < 2018):
        return False
    if(year > 2022):
        return False
    if(month > 12):
        return False
    if(month < 1):
        return False
    if(day > 31):
        return False
    if(day < 1):
        return False
    return dates