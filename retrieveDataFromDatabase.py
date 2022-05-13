import sys
import csv
from conversionFunctions import *
from datetime import datetime
from helperCheckInput import *
import os
from indexDictionary import *



def getCountyStateData(county, state):
    '''returns a list of data that fits the county and state from dataSet'''
    path = "Data/sub-Data/" + county + "," + state + ".csv" 
    return retrieveData(path)