from flask import Flask
from flask import render_template, request

#some helper functions to convert data to the inputs that our main code take
from conversionFunctions import *

import csv
import sys

app = Flask(__name__)

#Mock input
mockLocation = ["Rice", "Minnesota"]
mockDateRange = [['2021','2','1'], ['2021','3','1']]

#Mock Case data and date data from the dataset
mockDates = [['2021', '02', '01'], ['2021', '02', '02'], ['2021', '02', '03'], ['2021', '02', '04'], 
             ['2021', '02', '05'], ['2021', '02', '06'], ['2021', '02', '07'], ['2021', '02', '08'], 
             ['2021', '02', '09'], ['2021', '02', '10'], ['2021', '02', '11'], ['2021', '02', '12'], 
             ['2021', '02', '13'], ['2021', '02', '14'], ['2021', '02', '15'], ['2021', '02', '16'], 
             ['2021', '02', '17'], ['2021', '02', '18'], ['2021', '02', '19'], ['2021', '02', '20'], 
             ['2021', '02', '21'], ['2021', '02', '22'], ['2021', '02', '23'], ['2021', '02', '24'], 
             ['2021', '02', '25'], ['2021', '02', '26'], ['2021', '02', '27'], ['2021', '02', '28'], 
             ['2021', '03', '01']]

mockConfirmedCases = [6408, 6415, 6419, 6452, 6475, 6487, 6506, 6510, 6522, 6535, 6551, 6566, 6583, 6588, 
                      6594, 6598, 6601, 6614, 6622, 6629, 6632, 6638, 6641, 6642, 6653, 6664, 6671, 6690, 6700]

mockConfirmedDeaths = [78, 78, 82, 82, 82, 82, 82, 82, 83, 84, 84, 87, 87, 87, 87, 87, 87, 88, 
                       89, 89, 90, 90, 90, 91, 91, 91, 91, 91, 91]


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
    return render_template('graph.html', location = mockLocation, dateRange = mockDateRange, data = "mockOutput.png")

def getRawData(location, dateRange):
    '''
    renders a page for raw data based on mock data
    '''
    return render_template('rawdata.html', location = mockLocation, dateRange = mockDateRange, dates = mockDates, 
                           confirmedCases = mockConfirmedCases, confirmedDeaths = mockConfirmedDeaths)
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