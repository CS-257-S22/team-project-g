import sys
import csv
from conversionFunctions import *
from datetime import datetime
from helperCheckInput import *
import os
from indexDictionary import *
import psycopg2
import psqlConfig as config

def getCountyStateData(county, state):
    '''returns a list of data that fits the county and state from dataSet'''
    my_source = DataSource()
    return formatDatabaseData(my_source.getState(county,state))

def formatDatabaseData(data):
    datalist = []
    for row in data:
        row = list(row)
        row[0] = splitDate(row[0])
        datalist.append(row)
    return datalist



class DataSource:
    '''this is the object that connects the database to python code'''
    def __init__(self):
        '''this intlizes the variable that points to the database'''
        self.connection = self.connect()

    def connect(self):
        '''this opens the connection to the pesfied data base or returns an error if the data base cannot be reached'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    def getState(self,county,StateName):
        try:
            #set up a cursor
            cursor = self.connection.cursor()

            #make the query using %s as a placeholder for the variable
            query = "SELECT * FROM  CovidData WHERE StateName = %s and CountyName =%s ORDER BY day"

            #executing the query and saying that the magnitude variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (StateName,county))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

if __name__ == '__main__':
    getCountyStateData('Warren', 'Iowa')

