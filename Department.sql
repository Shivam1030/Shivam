CREATE DATABASE Department;
use Department;

CREATE TABLE department(
DeptID int,
Deptname VARCHAR(50));
insert into department VALUES (10,'RESEARCH'),
(20,'ACCOUNTING'),(30,'SALES'),(40,'OPERATIONS');

SELECT * FROM department;

SET SQL_SAFE_UPDATES=0;
drop TABLE department;

drop DATABASE Department;
drop TABLE department;