CREATE DATABASE college;
create database xyz_company;
drop database xyz_company;

USE college;

CREATE TABLE student(
 rollno INT,
 name VARCHAR(30),
 age INT
);

INSERT INTO student 
VALUES 
(101,"Jibitesh",58),
(102,"Ankita",1);

SELECT * FROM  student;