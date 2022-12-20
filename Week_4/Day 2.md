## SQL
***

### SELECT and FROM
```SQL
-- select every column from the country table 
SELECT * 
FROM country;
```

### WHERE
Conditionals
```SQL
SELECT * 
FROM country 
WHERE indepyear > 1980;
```

Two Contidionals
```SQL
SELECT name , 
	capital , 
	population , 
	indepyear as independent_year 
FROM country 
WHERE indepyear > 1980 
AND continent = 'Asia';
```

### ORDER BY
Orders Results
```SQL
SELECT name , 
	capital , 
	population , 
	indepyear as independent_year 
FROM country 
WHERE indepyear > 1980 
AND continent = 'Asia' 
ORDER BY population DESC;
```
### IN
```SQL
SELECT * 
FROM city 
WHERE name = 'Kabul' 
	OR name = 'Paris';
```

IN Version
```SQL
SELECT * 
FROM city 
WHERE name IN ('Kabul', 'Paris', 'Moscow');
```

### NOT IN
```SQL
-- Get every record that isn't the US or Germany 
SELECT * 
FROM country 
WHERE name NOT IN ('United States', 'Germany');
```

### ILIKE
```SQL
-- begin with only a single unknown letter
-- the next two letters are `er`
-- end with any number of other unknown letters
SELECT name
        , continent
FROM country
WHERE name ILIKE '_er%';
```

### JOIN (INNER JOIN)
```SQL
-- table_of_origin.column_name
SELECT city.name AS city_name,
        district, 
        country.name AS country_name,
        region
FROM city
JOIN country
  ON city.countrycode = country.code;
```

### SUBQUERY
```SQL
--Use a subquery to find the number of records in the `meals` table have the maximum price.
--Return one value in a column named `meal_count`.
select count(*)
from meals
where price = (select max(price)
				from meals);
```