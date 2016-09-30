Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

MySQL


SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(UPPER(CITY), 1) NOT IN ('A', 'E', 'I', 'O', 'U') AND
RIGHT(UPPER(CITY), 1) NOT IN ('A', 'E', 'I', 'O', 'U');
