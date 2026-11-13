USE prime;

CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
	order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101,1,500),
(102,1,900),
(103,2,300),
(104,5,700);

SELECT * FROM customers;

SELECT * FROM orders;

-- Inner Join --
SELECT * FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;

SELECT c.customer_id,o.order_id,c.name FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT JOIN --
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id;

-- RIGHT JOIN --
SELECT * 
FROM  customers c
RIGHT JOIN orders o
ON c.customer_id=o.customer_id;

-- OUTER JOIN(UNION)  --
SELECT *
FROM customers c 
LEFT JOIN orders o
ON c.customer_id=o.customer_id
UNION
SELECT *
FROM customers as c
RIGHT JOIN orders as o
ON c.customer_id=o.customer_id;

-- CROSS JOIN --
SELECT *
FROM customers c
CROSS JOIN orders o;

-- SELF JOIN[Works on Same Table]  --
SELECT *
FROM customers c 
JOIN customers d 
ON c.customer_id=d.customer_id;

-- LEFT EXCLUSIVE JOIN --
SELECT * 
FROM customers c
LEFT JOIN orders o 
ON c.customer_id=o.customer_id
WHERE o.customer_id IS NULL;

-- RIGHT EXCLUSIVE JOIN --
SELECT * 
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id=o.customer_id
WHERE c.customer_id IS NULL;