SELECT customerName, phone, city, country FROM customers LIMIT 10;

SELECT * FROM customers WHERE postalCode > 1370 OR salesRepEmployeeNumber > 150;

SELECT * FROM customers WHERE customerName LIKE "%mini%" LIMIT 10;

SELECT * FROM customers WHERE state = 'CA' OR state = 'NY' LIMIT 10;

SELECT * FROM customers WHERE creditLimit > 10000 LIMIT 10;
