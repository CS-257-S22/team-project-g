import array
from ast import Compare, If, Return
import compileall
from logging.config import valid_ident
from sre_parse import State
import sys
from tabnanny import check

state = 0
date = 1
help = "–state or -s “StateName” –daterange or -d “YYYY-MM-DD”’"

def getStateData(StateString):
    print(StateString)

def getDayData(dateRange):
    print(dateRange)

def setUpValidArguments():
    validArguments = {
        "-s" : state,
        "–state" : state,
        "-d" : date,
        "–daterange" : date,
        "-help" : help
    }
    return validArguments;

def getComadLine():
    arguments = sys.argv[1:];
    return arguments;

def compareArgument(argument):
    validArguments = setUpValidArguments()
    if (argument in (validArguments.keys())):
        return validArguments[argument]
    else: return False
    
def checkValidDate(date):
    DateList = date.split("-")
    if len(DateList) == 3:
        if (int(DateList[0]) > 2019) and (int(DateList[1]) <= 12) and (int(DateList[2]) <32): return DateList
    return False;

def CheckComadLineArg1(arguments):
    if compareArgument(str(arguments[0])) == state: return ("Please input state name, Try: -s texas")
    elif compareArgument(str(arguments[0])) == date: return ("Please input date, Try: -d 2020-1-1")
    elif compareArgument(str(arguments[0])) == help: return (help)
    elif compareArgument(str(arguments[0])) == False: return ("Not valid argument, Try: -help")

def CheckComadLineArg2(arguments):
    if compareArgument(str(arguments[0])) == state:
        return getStateData(arguments[1])
    if compareArgument(str(arguments[0])) == date:
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1")
        else: return getDayData(checkValidDate(str(arguments[1])))

def CheckComadLineArg3(arguments):
    if compareArgument(str(arguments[0])) == date: 
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        if checkValidDate(str(arguments[2])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([checkValidDate(str(arguments[1])),checkValidDate(str(arguments[2]))])
    else: return ("Not valid argument, Try: -help")

def CheckComadLineArg5(arguments):
    if compareArgument(str(arguments[0])) == state and compareArgument(str(arguments[1])) == date:
        if checkValidDate(str(arguments[3])) == False: return ("Please input valid date, Try: -d 2020-1-1")
        if checkValidDate(str(arguments[4])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([arguments[2],checkValidDate(str(arguments[3])),checkValidDate(str(arguments[4]))])


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
    else: return ("Not valid argument, Try: -help")
    



if __name__ == '__main__':
    arguments = getComadLine()
    print(CheckComadLine(arguments))
  
