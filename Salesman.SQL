CREATE TABLE IF NOT EXISTS Salesman(
    Salesman_id TEXT PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    COMISSION TEXT
);
INSERT INTO Salesman VALUES
    ('4005','James','Paris','0.13'),
    ('4006','Charles','Australia','0.5'),
    ('4002','Mc Lyon','New York','0.17'),
    ('4000','Paul Adam','Paris','0.11'),
    ('4003','Peter','USA','0.13'),
    ('4001','Lauson Hen','Rome','0.9');

SELECT *
FROM Salesman
WHERE NAME LIKE 'P%';

SELECT * FROM Salesman ORDER BY COMISSION DESC; 

SELECT MAX(COMISSION) AS MAXIMIUM_COMISSION FROM Salesman ;
SELECT MIN(COMISSION) AS MINIMUM_COMISSION FROM Salesman;

SELECT * FROM Salesman ORDER BY COMISSION ASC;

SELECT * FROM Salesman WHERE COMISSION > 0.2;
SELECT COUNT(Salesman_id) FROM Salesman WHERE COMISSION > 0.2;