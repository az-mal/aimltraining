-- Notes

-- Constraint and not null
-- Primary key: cannot be null and must be unique

use OurDB
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50)
)
select * from Emp
insert into Emp values (1,'Sam','Dicosta')
insert into Emp (Id,FName) values (2,'Rameez')
select * from Emp
insert into Emp (Id,Lname) values (6,"Khan") --will give error bcoz first name set to not null and must be included
insert into Emp (Id,Fname) values (2,"Deep") --cannot execute coz of duplicate primary key for the index

delete from Emp
select * from Emp


drop table Emp
select * from Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default('Kuala Lumpur')
)
insert into Emp values (1,'Sam','John','Brisbane')
insert into Emp values (2,'Rina','Kumari','Delhi')
select * from Emp
insert into Emp (Id,Fname,Lname) values(3,'Alina','Khan')
select * from Emp


drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default ('Kuala Lumpur'),
Salary float not null check(Salary>=10000 abd Salary<=50000)
)
insert into Emp (Id,Fname,Lname,Salary) values(3,'Alina','Khan',12000)
insert into Emp values (2,'Rina','Kumari','Delhi',9000)
-- the INSERT statement conflicted with the CHECK constraint "Ck_Emp_Salary_5165187F"
-- the conflict occured in database "OurDB", table "dbo.Emp",column 'Salary'
insert into Emp values (2,'Rina','Kumari','Delhi',69000)
-- the INSERT statement conflicted with the CHECK constraint "Ck_Emp_Salary_5165187F. The conflict occured

insert into Emp values (2,'Rina','Kumari','Delhi',19000)


drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10)
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
select * from Emp
insert into Emp values (1,'Maan','9876543210')
select * from Emp

insert into Emp values (3,'Riya','88999')
insert * from Emp(Id,Fname) values (3,'Riya')
insert into Emp values (4,'Rohan','9876543210')

drop table Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)

select * from Emp

alter table Emp add City nvarchar(50) not null

select * from Emp

alter table Emp drop column City

select * from Emp

drop table Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
insert into Emp values (1,'Sam','9876543210','sam@yahoo.com')
insert into Emp values (2,'Ravi','9876543210','sam@yahoo.com')
insert into Emp(Id,Fname,Mobile) values (3,'Ravi','9876543214')
select * from Emp
______________________________________________________________________________________________________

--identity(seed,increment)
create table Students
(SId int identity,
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Ravi',5000.50)
insert into Students(SName,SFee) values ('Ani',3000.50)
insert into Students(SName,SFee) values ('Joy',4500.20)
insert into Students(SName,SFee) values ('Riya',4500.20)

select * from Students

drop table Students


create table Salary
(Grade varchar(1) primary key,
BasicSalary float,
HRA as BasicSalary*0.10 persisted,
TA as BasicSalary*0.15 persisted,
DA as BasicSalary*0.20 persisted
)

insert into Salary values ('A',10000)
insert into Salary values ('B',5000)

select Grade,BasicSalary,HRA,TA,DA, BasicSalary+TA+DA+HRA as 'Net Salary' from Salary

insert into Salary values ('C',2000)
insert into Salary values ('D',1000)

select max(BasicSalary) from Salary
select min(BasicSalary) from Salary
select avg(BasicSalary) from Salary



select * from Salary

drop table Salary


_____________________________________________________________________________________________________


-----------------------------------------------------------------------------------------
-- Foreign Key
-----------------------------------------------------------------------------------------

CREATE TABLE Category
(
 CatId INT PRIMARY KEY,
 CategoryName NVARCHAR(50) NOT NULL UNIQUE
)

INSERT INTO Category VALUES (1, 'Electronics'),(2, 'Clothing'),(3, 'Home Decoration'),(4, 'Mobile')
SELECT * FROM Category ORDER BY CatId


CREATE TABLE Products
(
  PId INT PRIMARY KEY IDENTITY,
  PName NVARCHAR(50) NOT NULL,
  PPrice FLOAT NOT NULL,
  ProductCategory INT FOREIGN KEY REFERENCES Category
)

INSERT INTO Products VALUES ('Iphone', 5000, 4),('Nothing 3a', 2000, 4),('Washing Machine', 4000, 1),('Shirt', 200, 2),('T-Shirt', 199, 2), ('Jean', 399, 2)
SELECT * FROM Products
-----------------------------------------------
INSERT INTO Products VALUES('Remote', 209, 5)
-- The INSERT statement conflicted with the FOREIGN KEY constraint "FK_ProductsProduc_571DF1D5". The conflict occurred in database "OurDB", table "dbo.
--Category", column 'CatId'
-----------------------------------------------

SELECT * FROM Products JOIN Category ON Products.ProductCategory = Category.CatId

SELECT * FROM Products p JOIN Category c ON p.ProductCategory = c.CatId

SELECT p.PId, p.PName, p.PPrice, p.ProductCategory, c.CategoryName FROM Products p JOIN Category c ON p.ProductCategory = c.CatId

--for cosmetic if want to use better title for viewing purpose
SELECT p.PId 'Product Id', p.PName 'Product Name', p.PPrice 'Product Price', p.ProductCategory 'Category Id', c.CategoryName 'Category Name' FROM Products p JOIN Category c ON p.ProductCategory = c.CatId


create database SalesDb

use SalesDb

create table Products
(ProductID int primary key,
ProductName nvarchar(100),
Category nvarchar(50),
UnitPrice decimal(10,2)
)
insert into Products values (1,'Laptop Xiaomi','Electronics','4000'),('1200')


SELECT * FROM Category
DROP TABLE Category

SELECT * FROM Products
DROP TABLE Products