from flask import Flask, render_template
from CoreFunctions.helperCheckInput import helperCheckInput
from CoreFunctions.helperClasses import *
from CoreFunctions.displayGraph import displayGraph as renderGraphPage
from CoreFunctions.displayRawData import displayRawData as renderRawDataPage
from ProductionCode import CheckComadLine

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', title="CoViz")
    
"""
    Welcome To CoViz <br/> 
    We currently offer 2 ways to interact with the COVID data across the US <br/> 
                
        1. .../county/state/date1/date2 <br/> 
                
         Displays the confirmed cases and confirmed deaths for the specific location between date1 and date2<br/> 
         Try:<br/> 
         .../Rice/Minnesota/2020-2-1/2020-3-1<br/> 
                
         2. .../county/state/date1/date2/graph<br/> 
                
         Graphs the confirmed cases and confirmed deaths for the specific location between date1 and date2<br/> 
                
         Try:<br\> 
         .../Rice/Minnesota/2020-2-1/2020-3-1/graph<br/> 
"""

@app.route('/-s/<StateName>', strict_slashes=False)
def CommandLineState(StateName):
    """
    input string <StateName>
    """
    """
    uses Url to call get state
    """
    """
    return string of the row of the most recent cases of that state  
    """
    arguments = ["-s",StateName]
    outPut = CheckComadLine(arguments)
    return str(outPut)

@app.route('/-d/<Date>', strict_slashes=False)
def CommandLineDate(Date):
    """
    input string <date>
    """
    """
    uses Url to call get time date 
    """
    """
    return currently unimplmented 
    """
    arguments = ["-d",Date]
    outPut = CheckComadLine(arguments)
    return "Sorry Get Date not implemented yet"

@app.route('/<county>/<state>/<startDateString>/<endDateString>', strict_slashes=False)
def displayRawData(county,state,startDateString,endDateString):
    """
    Displays raw data, in text form, of cases and deaths during date range 
                                                in the location specified
    """
    validInput = helperCheckInput(county,state,startDateString,endDateString)
    if (validInput == True):
        dateRange = DateRange(startDateString,endDateString)
        location = Location(county,state)
        return renderRawDataPage(location, dateRange)
    else: 
        return makeErrorInputmsg(validInput)

@app.route('/<county>/<state>/<startDateString>/<endDateString>/graph', strict_slashes=False)
def graphImagePage(county,state,startDateString, endDateString):
    """ 
    Makes a graph with the input strings for county, state, start date, and end date. 
    """
    validInput = helperCheckInput(county,state,startDateString,endDateString)
    if (validInput == True):
        dateRange = DateRange(startDateString,endDateString)
        location = Location(county,state)

        return renderGraphPage(location, dateRange)
    else: 
        print(validInput)
        return makeErrorInputmsg(validInput)

def makeErrorInputmsg(checkInputResult):
    '''
    makes an error message based on the result from helperCheckInput
    input: checkInputResult, a list [] of error message(s)
    '''
    msg = ""
    for i in checkInputResult: 
        msg = msg + i + "<br>"
        
    return msg

@app.errorhandler(404)
def page_not_found(e):
    '''
    returns a 404 error page
    ''' 
    return render_template('PageNotFound.html', title="Page Not Found")

@app.errorhandler(500)
def python_bug(e):
    '''
    returns a 500 error page
    ''' 
    return "Sorry a bug happened. \n Try a new .../-s/Alabama/ "

if __name__ == '__main__':
    app.run()
