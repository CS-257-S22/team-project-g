import base64
from flask import Flask
import numpy as np
import sys
import io
import os
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
import makeGraph as mG
import helperMakeGraph as hMG

location = ["Autauga", "Alabama"] #placeholder for location, as we are still operating on a dummy dataset

app = Flask(__name__)

@app.route('/')
def homepage():
    '''Homepage, includes instructions'''
    return """
            In this function, you can get graphs of covid cases and deaths numbers to day<br/>
            Due to the fact that we are operating on a dummy data set, this apps is designed to display graphs for Autauga, Alabama<br/>
            Please input a start date and an end date in the route, in the following format:<br/>
            .../graph/startdate/enddate<br/>
            try:<br/>
            .../graph/2020-1-1/2020-12-1
            """

@app.route('/graph/<startDateString>/<endDateString>', strict_slashes=False)
def graphImagePage(startDateString, endDateString):
    ''' 
    Makes a graph with the input strings for start date and end date. 
    Prompt the user if the inputs are wrongly formatted. 
    '''
    
    if(not checkErrorInput(startDateString, endDateString) == True):
        return checkErrorInput(startDateString, endDateString)
    
    startDateList =  checkValidDate(startDateString)
    endDateList = checkValidDate (endDateString)
    
    return getData(startDateList, endDateList)

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

@app.errorhandler(404)
def page_not_found(e):
    '''Error message for not found'''
    return "Sorry, wrong format! Try .../graph/2020-1-1/2020-12-1"

@app.errorhandler(500)
def python_bug(e):
    '''Error message for python bug'''
    return "A bug in Python!"
 
def checkValidDate(dateString):
    '''
    A copy of checkValidDate() from production code due to error caused by imports
    
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

if __name__ == '__main__':
    app.run()
