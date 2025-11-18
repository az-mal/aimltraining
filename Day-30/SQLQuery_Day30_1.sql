create database ProductSalesDb
use ProductSalesDb
create table
(ProductId nvarchar(50) primary key,
ProductName nvarchar(50) not null,
Category nvarchar(50),
UnitPrice decimal(10,2)
)

create table Sales
(SalesId nvarchar(10) primary key,
ProductId nvarchar(50) not null foreign key references Products,
Quantity int not null,
TotalAmount decimal(12,2,),
SalesDate date
)
insert into Products values ('P-001','Laptop','Electronics',12000)
insert into Products values
('P-002','Washing Machine','Electronics',12000),
('P-003','Nothing-3a','Mobile',1800),
('P-004','Office-Chair','Furniture',500.50),
('P-005','Office-Desk','Electronics',700.25),
('P-006','Headphone','Electronics',150),
('P-007','Touch Screen','Electronics',2000),
('P-010','Iphone-17','Mobile',5800)
select * from Products

insert into Sales values ('S-001','P-001',2*(select UnitPrice from Products),'2025-01-15')