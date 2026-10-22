/*
Qs: Create a database for your college.

Create a table named Teacher to store (id, name, subject, salary).

Insert the following data into the table:

23, "ajay", "math", 50000
47, "bharat", "english", 60000
18, "chetan", "chemistry", 45000
9, "divya", "physics", 75000

Practice Questions

1. Select teachers whose salary is more than 55K.
2. Rename the salary column of the Teacher table to ctc.
3. Update the salary of all teachers by giving them an increment of 25%.
4. Add a new column for teachers called city.
   The default city should be "Gurgaon".
5. Delete the salary column from the Teacher table.
*/


CREATE DATABASE IF NOT EXISTS college;
USE college;

CREATE TABLE Teacher(
 id INT PRIMARY KEY,
 name VARCHAR(20) ,
 subject VARCHAR(20),
 salary INT);
 
INSERT INTO Teacher
(id,name,subject,salary)
VALUES
(23,"ajay","math",50000),
(47,"bharat","english",60000),
(18,"chetan","chemistry",45000),
(9,"divya","physics",75000);
 

SELECT * FROM Teacher;
 
-- 1)
Select *
FROM Teacher
WHERE salary>55000;

-- 2)
ALTER TABLE Teacher
CHANGE COLUMN salary ctc INT;

 
SET SQL_SAFE_UPDATES=0;
 
-- 3)
UPDATE Teacher
SET ctc = ctc + ctc* 0.25;

-- 4)
ALTER TABLE Teacher
ADD COLUMN city VARCHAR(20) DEFAULT "Gurgaon";

-- 5)
ALTER TABLE Teacher
DROP COLUMN ctc;

SELECT * FROM Teacher;
 


