CREATE TABLE players (
    id INT PRIMARY KEY,
    name TEXT,
    number INT,
    age INT
);

INSERT INTO players (id, name, number, age) VALUES
(1, 'LeBron James', 23, 40),
(2, 'Stephen Curry', 30, 37),
(3, 'Kevin Durant', 7, 36),
(4, 'Giannis Antetokounmpo', 34, 30),
(5, 'Luka Doncic', 77, 26),
(6, 'Jayson Tatum', 0, 27);

SELECT * FROM players;

SELECT name, number FROM players;

SELECT * FROM players
WHERE age > 30;

SELECT * FROM players
WHERE number = 23;

SELECT * FROM players
WHERE name LIKE 'S%';

SELECT * FROM players
WHERE name LIKE '%James%';

SELECT MIN(age) AS youngest_player FROM players;

SELECT MAX(age) AS oldest_player FROM players;

SELECT MIN(number) AS smallest_jersey FROM players;

SELECT MAX(number) AS largest_jersey FROM players;

SELECT COUNT(*) AS total_players FROM players;

SELECT AVG(age) AS average_age FROM players;

SELECT * FROM players
ORDER BY age DESC;

SELECT name, age
FROM players
WHERE age = (SELECT MAX(age) FROM players);