-- create onject onjectName

create database OurDB

-- create tab;e <TableName>
-- column datatype

use OurDB

create table Student
(SId int primary key,
SName nvarchar(50) not null,
SFee float not null)

select * from Student
insert into Student values (1,'Sam',500.50)
insert into Student values
(2,'Rohit',4500.25),
(3,'Neha',5000.58),
(4,'Aini',6600.27),
(5,'Arisha',4000.28)