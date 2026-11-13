SELECT @@autocommit;

SET autocommit=0;

CREATE DATABASE prime;
USE prime;

CREATE TABLE accounts(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance DECIMAL(10,2)
);

INSERT INTO accounts
(name, balance) -- By Default id taken 
VALUES
("Adam", 500.00),
("Bob", 300.00),
("Charlie", 1000.00);

SELECT * FROM accounts;

-- Transactions --
START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id=1;
UPDATE accounts SET balance = balance + 50 WHERE id=2;

COMMIT;
ROLLBACK; -- But No change as already commited. 

SELECT * FROM accounts;

-- RollBack(Only Applicable on Uncommited Changes --

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id=1;
UPDATE accounts SET balance = balance + 50 WHERE id=2;
-- No Commit 
ROLLBACK; 

SELECT * FROM accounts;

-- SaVePoint --
START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id=1;
SAVEPOINT after_wallet_topup; 

UPDATE accounts SET balance = balance + 10 WHERE id=1; 
-- Error
ROLLBACK TO after_wallet_topup;
COMMIT;

SELECT * FROM accounts;



