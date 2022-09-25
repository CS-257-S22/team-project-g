DROP TABLE IF EXISTS covidData;
CREATE TABLE covidData (
  Date date,
  CountyName text,
  StateName text,
  ConfirmedCases int,
  ConfirmedDeaths int
);
