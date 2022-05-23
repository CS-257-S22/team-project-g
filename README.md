# Team G - CoViz: Visualizations of United States COVID-19 Data
Team members: Bryan, Dake, Sam, Will

!!! To check projects before Team Back End, change the isOnServer variable in settings.py to False!!!

1. Command Line Project: run ProductionCode.py; Run python3 ProductionCode.py --help for help, or see instructions below

Instructions:

Examples of things you can do: 

    1. Get the latest number of COVID cases in a state (inaccurate number right now, due to the fact that we are using dummy data):

        Try:
            python3 ProductionCode.py Rice Minnesota 2020-2-1 2020-4-1

    2. Get the graph of the COVID cases and deaths in a county within a date range:

        Try:
            python3 ProductionCode.py Rice Minnesota 2020-2-1 2021-4-1 -g

2. FlaskApp: run FlaskApp.py; Instructions on the homepage

3. Front End Component: run BasicFrontEnd.py, instructions on the webpage

    Note: 
    BasicFrontEndAuto.py 
    templates/autocomplete.html
    templates/autoConplete copy.html
    are still in progress and are not a part of this submission

!!! To check projects after (including) Team Back End, change the isOnServer variable in settings.py to True!!!

4. Team Back End: 

    a. View CoreFunctions/retrieveDataFromDatabase.py --- this is originally a (and the only) function in retrievedata.py that reads from .csv files. It is now modified to retrieve data from the back end database and called in retrieveData.py 
    b. Run BasicFrontEnd.py to check if this function works --- it is indirectly called in our front end function. 
    c. CoreFunctions/RetireveDataFromLocal.py is our original function that uses .csv files, it is now used for previous versions and tests only.
    
    d. Command to copy file:
    \copy covidData FROM 'us_simplified_cleaned.csv' DELIMITER ',' CSV 