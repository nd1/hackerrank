Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

MySQL


SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(UPPER(CITY), 1) NOT IN ('A', 'E', 'I', 'O', 'U') OR
RIGHT(UPPER(CITY), 1) NOT IN ('A', 'E', 'I', 'O', 'U');
