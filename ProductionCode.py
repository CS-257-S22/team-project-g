from inspect import ArgSpec
import sys

from click import argument
import makeGraph as mG
import helperCheckInput as hCI
from conversionFunctions import *
import displayRawData as dRD
import argparse

def CheckComadLine(argv):
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
    outPut = hCI.helperCheckInput(args.County,args.State,args.StartDate, args.EndDate)
    if outPut == True:
        location = makeLocation(args.County,args.State)
        dateRange = makedateRange(args.StartDate, args.EndDate)
        if args.graph:
           return mG.makeGraph(location,dateRange)
        else: 
            return dRD.displayRawData(location,dateRange)
    else: return outPut

    
if __name__ == '__main__':
    outPut = callData(CheckComadLine(sys.argv[1:]))
    
    if isinstance(outPut,str):
        #check if the result is a string
        outPut = outPut.split('<br/>')
    if isinstance(outPut,str):
        #check if output is an error message
        print(outPut)
    elif isinstance(outPut,list):
        #check if output is a list, if so, it is the result of displayRawData, print the result
        for row in outPut:
            print(row)

  
