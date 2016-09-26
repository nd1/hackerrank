**Task**: Query the names of all American cities in CITY with populations larger than 120,000. The CountryCode for America is USA.

**Query**
SELECT NAME
FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION > 120000;
