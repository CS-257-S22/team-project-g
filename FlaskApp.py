from flask import Flask
import displayGraph as fH
import helperCheckInput as hCI
import ProductionCode as pC
import displayGraph as dG

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome To CoViz \n Due to the problems with printing a graph \n only the get state function is usable \n url /-s/StateName is the format to Acess get state Data \n try -s/Alabama/ "

@app.route('/-s/<StateName>', strict_slashes=False)
def CommandLineState(StateName):
    arguments = ["-s",StateName]
    outPut = pC.CheckComadLine(arguments)
    return str(outPut)

@app.route('/-d/<Date>', strict_slashes=False)
def CommandLineDate(Date):
    arguments = ["-d",Date]
    outPut = pC.CheckComadLine(arguments)
    return "Sorry Get Date not implemented yet"

@app.route('/<county>/<state>/<startDateString>/<endDateString>/graph', strict_slashes=False)
def graphImagePage(county,state,startDateString, endDateString):
    ''' 
    Makes a graph with the input strings for start date and end date. 
    Prompt the user if the inputs are wrongly formatted. 
    '''

    startDateList =  hCI.checkValidDate(startDateString)
    endDateList = hCI.checkValidDate (endDateString)
    dateRange = [startDateList, endDateList]
    location = [county, state]
    
    return dG.displayGraph(location, dateRange)


@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format, \n Try: try url -s/Alabama/ "

@app.errorhandler(500)
def python_bug(e):
    return "Sorry a bug happened. \n Try a new Url -s/Alabama/ "

if __name__ == '__main__':
    app.run()