Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

MySQL

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(UPPER(CITY), 1) in ('A', 'E', 'I', 'O', 'U') AND
RIGHT(UPPER(CITY), 1) in ('A', 'E', 'I', 'O', 'U');
