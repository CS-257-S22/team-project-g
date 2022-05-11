DROP TABLE IF EXISTS covidData;
CREATE TABLE covidData (
  Day date,
  CountyName text,
  StateName text,
  ConfirmedCases int,
  ConfirmedDeaths int
);
