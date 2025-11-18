CREATE DATABASE ExerciseOne;
USE ExerciseOne;
create table StudentMarks (
    StudentID int,
    StudentName nvarchar(50),
    Math int,
    Science int,
    English int,
    History int
)

INSERT INTO StudentMarks VALUES
(1,'Sam',90,85,90,88)

INSERT INTO StudentMarks VALUES
(2,'Atif',85,90,78,85),
(3,'Chang',75,85,80,77),
(4,'Vi',93,91,91,98),
(5,'Ani',90,78,93,86),
(6,'Riya',67,75,92,78)


SELECT * FROM  StudentMarks
DELETE FROM StudentMarks
DROP TABLE StudentMarks