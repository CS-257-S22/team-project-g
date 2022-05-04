from flask import Flask
from flask import render_template, request
import displayGraph as dG
#some helper functions to convert data to the inputs that our main code take
from conversionFunctions import *

import csv
import sys

app = Flask(__name__)

@app.route('/')
def homepage():
    '''homepage'''
    return render_template('home.html')

@app.route('/displayRawData')
def displayRawData():
    ''' 
    function to display the page with raw data
    takes information from form and calls relative functions with the data
    '''
    state = str(request.args['state'])
    county = str(request.args['county'])
    startDate = str(request.args['startDate'])
    endDate = str(request.args['endDate'])
    location = makeLocation(county, state)
    dateRange = makedateRange(startDate,endDate)
    
    return getRawData(location, dateRange)

@app.route('/displayGraph')
def displayGraph():
    ''' 
    function to display the page with graphs
    takes information from form and calls relative functions with the data
    '''
    state = str(request.args['state'])
    county = str(request.args['county'])
    startDate = str(request.args['startDate'])
    endDate = str(request.args['endDate'])
    location = makeLocation(county, state)
    dateRange = makedateRange(startDate,endDate)
    # return dG.displayGraph(location, dateRange)
    return getGraph(location, dateRange)

def getGraph(location, dateRange):
    '''
    renders a page for graphs based on mock data
    '''
    return dG.displayGraph(location, dateRange)

def getRawData(location, dateRange):
    
    return render_template('rawdata.html', location = location, dateRange = dateRange)

@app.errorhandler(404)
def page_not_found(e):
    '''
    renders a page not found page
    '''
    return render_template('pagenotfound.html')

@app.errorhandler(500)
def python_bug(e):
    '''
    renders an internal error page
    '''
    return render_template('internalerror.html')

if __name__ == '__main__':
    app.run()