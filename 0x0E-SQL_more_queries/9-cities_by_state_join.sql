--  script that lists all cities contained in the database hbtn_0d_usa.
-- using inner join
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states 
ON cities.states.id = states.id
ORDER BY cities.id;
