# Team G - CoViz: Visualizations of United States COVID-19 Data
Team members: Bryan, Dake, Sam, Will

Command Line Project: run ProductionCode.py; Run python3 ProductionCode.py --help, or see usage.txt for instructions

FlaskApp: run FlaskApp.py; Instructions on the homepage

Front End Component: run BasicFrontEnd.py, instructions on the webpage

    Note: 
    BasicFrontEndAuto.py 
    templates/autocomplete.html
    templates/autoConplete copy.html
    are still in progress and are not a part of this submission

Team Back End: 
1. View retrieveDataFromDatabase.py --- this is originally a (and the only) function in retrievedata.py that feads from .csv files. It is now modified to retrieve data from the back end database and called in retrieveData.py 
2. Run BasicFromtEnd.py to check if this function works --- it is indirectly called in our front end function. 
3. RetireveDataFromLocal.py is our original function that uses .csv files, it is now used for previous tests only.
Command to copy file:
    \copy covidData FROM 'us_simplified_cleaned.csv' DELIMITER ',' CSV 