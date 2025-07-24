Create table supplier (
    SID TEXT PRIMARY KEY,
    SFOOD TEXT,
    PRICE INTEGER,
    NUMBEROFORDERS TEXT
);

Insert into supplier (SID, SFOOD, PRICE, NUMBEROFORDERS) VALUES
    ('951', 'fries', 2000, '2'),
    ('345', 'burger', 1500, '4'),
    ('289', 'pizza', 3500, '3'),
    ('456', 'soda', 170, '5'),
    ('509', 'chicken', 2630, '6');

SELECT * FROM supplier;

SELECT * FROM supplier WHERE NUMBEROFORDERS TEXT > '3';
SELECT * FROM supplier ORDER BY PRICE ASC;

SELECT * FROM supplier WHERE SFOOD = 'fries';

SELECT SUM(PRICE) AS Total_Price
FROM supplier;