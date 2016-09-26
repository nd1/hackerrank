Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

MySQL


SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(UPPER(CITY), 1) in ('A', 'E', 'I', 'O', 'U');
