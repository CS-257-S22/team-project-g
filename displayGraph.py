import csv
from flask import Flask
import io
import makeGraph as mG
import os
import sys
import base64
from flask import render_template
from helperCheckInput import *

def displayGraph(location, dateRange):
    return getData(location, dateRange)

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

def getData(location, dateRange):
    '''
    get image data from makeGraph
    
    input: a location and a dateRange that 
    
    output: "Data Not Found!" if no information is found
            image data if the input is correctly formatted and the information is in database
    '''
    output = io.BytesIO()
    
    isData = mG.make2GraphToOutPut(location,dateRange,output)
    if(not(isData)):
        return "Data Not Found!"
    
    data = base64.b64encode(output.getvalue()).decode('utf-8 ')
    return data

def getHTML(location, dateRange):
    ''' 
    returns a rendered HTML page according to a location and a dateRange    
    '''
    data = getData(location, dateRange)
    return render_template('graph.html', location = location, dateRange = dateRange,data = data)
