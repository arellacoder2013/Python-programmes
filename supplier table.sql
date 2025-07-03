CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
    ('S1', 'Smith', 20, 'London'),
    ('S2', 'Jones', 10, 'Paris'),
    ('S3', 'Blake', 30, 'Paris'),
    ('S4', 'Clarke', 20, 'London'),
    ('S5', 'Adams', 30, 'Athens');

SELECT * FROM supplier;


Create table supplier0 (
    SID TEXT PRIMARY KEY,
    SFOOD TEXT,
    PRICE INTEGER,
    NUMBEROFORDERS TEXT
);

Insert into supplier0 (SID, SFOOD, PRICE, NUMBEROFORDERS) VALUES
    ('951', 'fries', 2000, '2'),
    ('345', 'burger', 1500, '4'),
    ('289', 'pizza', 3500, '3'),
    ('456', 'soda', 170, '5'),
    ('509', 'chicken', 2630, '6');

SELECT * FROM supplier0;