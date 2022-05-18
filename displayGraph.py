#makes a rendered html page based on a input location and dateRange
import csv
from flask import Flask
import io
import makeGraph as mG
import os
import sys
import base64
from flask import render_template

def displayGraph(location, dateRange):
    return getHTML(location, dateRange)

def getData(location, dateRange):
    """
    get image data from makeGraph
    
    input:  location [county, state]
            dateRange [[Year, Month, Date],[Year, Month, Date]]
    
    output: data [confirmedCasesGraph, confirmedDeathsGraph], a list of two graphs in streamIO()
    """
    
    output = mG.makeSeperateGraphs(location,dateRange)
    
    confirmedCasesGraph = base64.b64encode(output[0].getvalue()).decode('utf-8 ')
    confirmedDeathsGraph = base64.b64encode(output[1].getvalue()).decode('utf-8 ')
    data = [confirmedCasesGraph, confirmedDeathsGraph]
    return data

def getHTML(location, dateRange):
    """ 
    returns a rendered HTML page with 2 graphs according to a location and a dateRange  
    
    input:  location [county, state]
            dateRange [[Year, Month, Date],[Year, Month, Date]]  
    """
    data = getData(location, dateRange)
    return render_template('graph.html', location = location, dateRange = dateRange, 
                           confirmedCasesGraph = data[0], confirmedDeathsGraph = data[1])
