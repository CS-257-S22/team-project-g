from flask import Flask
from flask import render_template, request
import displayGraph as dG
import helperCheckInput as hCI
import retrieveData as rD
#some helper functions to convert data to the inputs that our main code take
from helperClasses import *
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
    checkInputResult = hCI.helperCheckInput(county,state,startDate,endDate)
    if (checkInputResult == True):
        dateRange = DateRange(startDate,endDate)
        location = Location(county,state)
        return getRawData(location, dateRange)
    else: 
        return errorInputPrompt(checkInputResult)

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
    checkInputResult = hCI.helperCheckInput(county,state,startDate,endDate)
    if (checkInputResult == True):
        dateRange = DateRange(startDate,endDate)
        location = Location(county,state)
        return dG.displayGraph(location, dateRange)
    else: 
        return errorInputPrompt(checkInputResult)
    
def errorInputPrompt(errormsg):
    '''
    renders a error page with an error message 
    ''' 
    return render_template('errorinput.html', errormsg = errormsg)

def getGraph(location, dateRange):
    '''
    renders a page for graphs based on location and dateRange
    '''
    return dG.displayGraph(location, dateRange)

def getRawData(location, dateRange):
    '''
    renders a page for raw data based on location and dateRange
    '''
    data = rD.getDataWithLocationAndDateRange(location,dateRange)
    return render_template('rawdata.html', location = location, dateRange = dateRange, 
                           dates = rD.getDates(data), confirmedCases = rD.getConfirmedCases(data), 
                           confirmedDeaths = rD.getConfirmedDeaths(data))

@app.errorhandler(404)
def page_not_found(e):
    '''
    renders a page not found page
    '''
    return render_template('PageNotFound.html')

@app.errorhandler(500)
def python_bug(e):
    '''
    renders an internal error page
    '''
    return render_template('internalerror.html')

if __name__ == '__main__':
    app.run(host = "localhost", port = 5125)