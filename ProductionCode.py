import argparse
import sys
from CoreFunctions.makeGraph import *
from CoreFunctions.helperCheckInput import *
from CoreFunctions.displayRawData import *
from CoreFunctions.helperClasses import *

def CheckComadLine(argv):
    '''in put comand lines String county String state  String start-date String End-date'''
    '''looks for the graph flag and the input strings'''
    '''Out put an object with the inputs as named variables'''
    parser = argparse.ArgumentParser(description='Please enter the following in the order they are shown for raw data, and add -g for graphs.')
    parser.add_argument('County',type=str,
                        help='The Name of the county to be looked up')
    parser.add_argument('State',type=str,
                        help='The Name of the state to be looked up')
    parser.add_argument('StartDate',type=str,
                        help='The begining of the date range to look through, in the format YYYY-MM-DD')
    parser.add_argument('EndDate',type=str,
                        help='THe end of the date range to look through, in the format YYYY-MM-DD')
    parser.add_argument('-g','--graph',action='store_true',
        help= 'The flag to graph Data')
    args = parser.parse_args(argv)
    return args


def callData(args):
    '''input args.Parser object'''
    '''call main function deppending on graph flag '''
    ''' return string of state data or graph out put'''
    outPut = helperCheckInput(args.County,args.State,args.StartDate, args.EndDate)
    if outPut == True:
        location = Location(args.County,args.State)
        dateRange = DateRange(args.StartDate, args.EndDate)
        if args.graph:
           return makeGraph(location,dateRange)
        else: 
            return displayRawData(location,dateRange)
    else: return outPut

    
if __name__ == '__main__':
    outPut = callData(CheckComadLine(sys.argv[1:]))
    # if output is a string (the function called is getrawdata), split it with <br/> (line break in html), and print each line
    if isinstance(outPut,str):
        outPut = outPut.split('<br/>')
        for row in outPut:
            print(row)
    # if output is a list (the check functions reported errors), print each error
    elif isinstance(outPut,list):
        for row in outPut:
            print(row)
  
