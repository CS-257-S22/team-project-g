from sre_compile import isstring
import sys

import retrieveData as rD
import makeGraph as mG
import getDayWithMostCases as gDMC

state = 0
date = 1
graph = 2
help = """Welcome to Coviz, a program that provides informtion and visualization for COVID-19 cases\n
–-state or -s “StateName” returns the highest number of confirmed cases in a given state
--date or -d "YYYY-MM-DD" returns the information of confirmed cases and deaths on a given day
--daterange or -d “YYYY-MM-DD” “YYYY-MM-DD” returns information of confirmed cases and deaths between 2 given dates"""
#–-state or -s “StateName” –-daterange or -d “YYYY-MM-DD” “YYYY-MM-DD” returns graphs of the number of cases and deaths in the given State over a time span

def getStateData(stateName):
    gDMC.getDayWithMostCases(stateName)

def getDayData(dateRange):
    print(dateRange)

def makeGraphOfData(location, startDate, endDate):
    mG.makeGraph(location,[startDate,endDate])
    

def CheckComadLine(arguments):
    if (len(arguments) <= 0): return ("No arguments, Try -s or -d")
    elif (len(arguments) == 1):
        return CheckComadLineArg1(arguments)
    elif (len(arguments) == 2) and arguments[1] != "-d":
        return  CheckComadLineArg2(arguments)
    elif (len(arguments) == 3):
        return CheckComadLineArg3(arguments)
    elif (len(arguments) == 5):
        return CheckComadLineArg5(arguments)
    else: return ("Not valid argument, Try: --help")

def setUpValidArguments():
    #create dictonary of commands 
    validArguments = {
        "-s" : state,
        "-–state" : state,
        #"-c": county,
        #"--county": county,
        "-d" : date,
        "-–daterange" : date,
        "--help" : help
    }
    return validArguments

def getComadLine():
    #To get valid comand lines converet comand converet sys.argv into string
    arguments = sys.argv[1:]
    return arguments


def compareArgument(argument):
    #check string aganst valid comands 
    validArguments = setUpValidArguments()
    if (argument in (validArguments.keys())):
        return validArguments[argument]
    else: return False
    
def checkValidDate(date):
    #check data in put for valid year month and day 
    DateList = date.split("-")
    if len(DateList) == 3:
        if (int(DateList[0]) > 2019) and (int(DateList[1]) <= 12) and (int(DateList[2]) <32): return DateList
    return False

def CheckComadLineArg1(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == state: return ("Please input state name, Try: -s texas")
    elif compareArgument(str(arguments[0])) == date: return ("Please input date, Try: -d 2020-1-1")
    elif compareArgument(str(arguments[0])) == help: return (help)
    elif compareArgument(str(arguments[0])) == False: return ("Not valid argument, Try: --help")

def CheckComadLineArg2(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == state:
        return getStateData(arguments[1])
    if compareArgument(str(arguments[0])) == date:
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1")
    else: 
        return getDayData(checkValidDate(str(arguments[1])))

def CheckComadLineArg3(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == date: 
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        if checkValidDate(str(arguments[2])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([checkValidDate(str(arguments[1])),checkValidDate(str(arguments[2]))])
    else: return ("Not valid argument, Try: --help")

def CheckComadLineArg5(arguments):
    if compareArgument(str(arguments[0])) == state and compareArgument(str(arguments[1])) == date:
        if checkValidDate(str(arguments[3])) == False: return ("Please input valid date, Try: -d 2020-1-1")
        if checkValidDate(str(arguments[4])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([arguments[2],checkValidDate(str(arguments[3])),checkValidDate(str(arguments[4]))])
    else: return ("Not valid argument, Try: --help")
    
if __name__ == '__main__':
    arguments = getComadLine()
    outPut = CheckComadLine(arguments)
    if isstring(outPut):
        print(outPut)
  
