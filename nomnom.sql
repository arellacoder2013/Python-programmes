CREATE TABLE IF NOT EXISTS NOMNOM (
    NAME TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVIEW TEXT,
    PRICE TEXT,
    HEALTH TEXT
);

INSERT INTO NOMNOM VALUES
    ('Peter','Brooklyn','Steak',4.4,'$$$$','A'),
    ('Jamie','Midtown','Korean',3.5,'$$','A'),
    ('Kate','Midtown','Chinese',5,'$$$','B'),
    ('Leila Palace','Queens','Pizza',3.9,'$','A'),
    ('Maria','Downtown','American',3.9,'$$$',''),
    ('Samara','Chinatown','Chinese',3.2,'$$','');

SELECT * FROM NOMNOM;
SELECT DISTINCT NEIGHBOURHOOD FROM NOMNOM; 

SELECT DISTINCT CUISINE FROM NOMNOM;

SELECT * FROM NOMNOM WHERE CUISINE = 'Chinese';

SELECT * FROM NOMNOM WHERE REVIEW > 4;

SELECT * FROM NOMNOM WHERE CUISINE = 'Chinese' AND PRICE ='$$$';

SELECT * FROM NOMNOM WHERE NAME LIKE '%Palace%';

SELECT * FROM NOMNOM WHERE NEIGHBOURHOOD IN('Midtown','Chinatown','Downtown');

SELECT * FROM NOMNOM ORDER BY REVIEW DESC LIMIT 4;

SELECT * FROM NOMNOM WHERE CUISINE = 'Chinese' AND REVIEW >= 3.5;