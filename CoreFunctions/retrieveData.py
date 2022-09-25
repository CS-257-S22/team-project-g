#A function that retrieves data from local or online database
#Switches between online and local databases based on setting 
from CoreFunctions.conversionFunctions import *
from CoreFunctions.indexDictionary import *
from CoreFunctions.helperClasses import *

#use the database if operating on server, else use the local .csv files
import settings

if (settings.isOnServer):
    from CoreFunctions.retrieveDataFromDatabase import getDataCombination
else:
    from CoreFunctions.retrieveDataFromLocal import getDataCombination

