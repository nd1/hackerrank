**Task**: Query all columns for all American cities in CITY with populations larger than 100,000. The CountryCode for America is USA.

**Query**:
SELECT *
FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION > 100000;
