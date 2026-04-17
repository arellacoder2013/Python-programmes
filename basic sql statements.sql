
CREATE TABLE students (
    id INT PRIMARY KEY,
    name TEXT,
    age INT,
    grade TEXT
);


INSERT INTO students (id, name, age, grade) VALUES
(1, 'Alice', 20, 'A'),
(2, 'Brian', 17, 'B'),
(3, 'Catherine', 22, 'A'),
(4, 'Daniel', 19, 'C'),
(5, 'Ethan', 21, 'B'),
(6, 'Ann', 18, 'A');


SELECT * FROM students;

SELECT name, age FROM students;


SELECT * FROM students
WHERE age > 18;

SELECT * FROM students
WHERE grade = 'A';


SELECT * FROM students
WHERE name LIKE 'A%';

SELECT * FROM students
WHERE name LIKE '%n';

SELECT * FROM students
WHERE name LIKE '%an%';


SELECT MIN(age) AS youngest FROM students;

SELECT MAX(age) AS oldest FROM students;


SELECT COUNT(*) AS total_students FROM students;

SELECT AVG(age) AS average_age FROM students;

SELECT * FROM students
ORDER BY age DESC;

SELECT name, age
FROM students
WHERE age = (SELECT MAX(age) FROM students);