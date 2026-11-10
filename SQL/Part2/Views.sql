USE prime;

SELECT * FROM customers;
SELECT * FROM orders;

CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM view1 WHERE name="Alice";

/*
CREATE VIEW view2 AS 
SELECT * 
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;
*/ 
-- ERROR:- We can't print column having same name in 2 different table

CREATE VIEW view2 AS 
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

SELECT * FROM view2;
