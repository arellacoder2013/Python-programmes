CREATE TABLE IF NOT EXISTS BOOKS (
    NAME TEXT,
    NEIGHBOURHOOD TEXT,
    AUTHOR TEXT,
    PRICE TEXT,
    NAMEOFBOOK TEXT
);

INSERT INTO BOOKS VALUES
    ('James','Brooklyn','Harper Lee',11.80,'To Kill a Mockingbird'),
    ('Jamie','Midtown','J.K. Rowling',14.99,'Harry Potter and the Sorcerer’s Stone'),
    ('Kate','Midtown','Jeff Kinney ',9.99,'Diary of a Wimpy Kid'),
    ('Leila','Queens','Roald Dahl ',8.50,'Charlie and the Chocolate Factory'),
    ('Maria','Downtown','Neil Gaiman',8.75,'Coraline'),
    ('Samara','Chinatown','J.K. Rowling',10.99,'Harry Potter and the Prisoner of Azkaban');

SELECT * FROM BOOKS;
SELECT DISTINCT NEIGHBOURHOOD FROM BOOKS; 

SELECT *
FROM BOOKS
WHERE NAME LIKE 'J%';

SELECT * FROM BOOKS WHERE PRICE > 9;

SELECT * FROM BOOKS WHERE AUTHOR = 'J.K. Rowling';

SELECT * FROM BOOKS WHERE NAMEOFBOOK LIKE '%Harry Potter%';

SELECT * FROM BOOKS WHERE NEIGHBOURHOOD IN('Midtown','Chinatown','Downtown');

SELECT * FROM BOOKS ORDER BY PRICE DESC LIMIT 4;

SELECT * FROM BOOKS WHERE PRICE = 8.50 AND NAMEOFBOOK  LIKE '%Chocolate Factory%';

SELECT SUM(PRICE) AS Total_Price
FROM BOOKS;

SELECT MAX(PRICE) AS Most_expensive FROM BOOKS;
SELECT MIN(PRICE) AS Least_expensive FROM BOOKS;