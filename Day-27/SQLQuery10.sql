CREATE DATABASE SalesDb

USE SalesDb

CREATE TABLE Products
(ProductID int primary key,
ProductName nvarchar(100),
Category nvarchar(50),
UnitPrice decimal(10,2)
)

INSERT INTO Products VALUES
(1,'Laptop Xiaomi','Electronics',1200),
(2,'Wireless Keyboard','Electronics',400),
(3,'Wireless Mouse','Electronics',200),
(4,'Table','Furniture',600),
(5,'Notebook','Stationary',250),
(6,'Bed','Furniture',1300),
(7,'Penbox','Stationary',10.50)


SELECT * FROM  Products
DELETE FROM Products
DROP TABLE Products

CREATE TABLE Sales
(SalesID int primary key identity,
ProductID int foreign key references Products(ProductID),
Region nvarchar(50) check (Region in ('East','West','North','South')),
Quantity int,
SalesDate date
)

insert into Sales 
(ProductId,Region,Quantity,SalesDate) 
values (3,'West',15,'2024-02-23'),
(2,'East',10,'2024-02-23'),
(3,'North',5,'2024-02-20'),
(4,'South',6,'2024-02-24'),
(4,'West',10,'2024-03-23'),
(5,'West',12,'2024-01-23'),
(6,'East',4,'2024-02-24')


INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
(1, 'East', 5, '2024-01-10'),
(2, 'West', 10, '2024-01-12'),
(3, 'North', 3, '2024-02-05'),
(4, 'South', 8, '2024-02-10'),
(5, 'East', 2, '2024-03-01'),
(1, 'West', 7, '2024-03-15'),
(3, 'North', 4, '2024-04-03'),
(2, 'South', 6, '2024-04-10'),
(5, 'East', 3, '2024-05-02'),
(4, 'West', 9, '2024-05-10')


SELECT * FROM  Sales
DELETE FROM Sales
DROP TABLE Sales