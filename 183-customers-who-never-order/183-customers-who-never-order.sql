# Write your MySQL query statement below

#SELECT Customers.name form Customers where Customers.id NOT IN (SELECT o.customerId from Orders o);

SELECT c.name AS Customers from Customers c LEFT JOIN Orders o ON c.id = o.customerId where o.customerId IS NULL;