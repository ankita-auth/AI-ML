Use prime;

ALTER TABLE accounts
ADD BRANCH VARCHAR(20);

UPDATE  accounts
SET BRANCH="Mumbai"
WHERE id=1;

UPDATE  accounts
SET BRANCH="Delhi"
WHERE id=2;

UPDATE  accounts
SET BRANCH="Bangalore"
WHERE id=3;

INSERT INTO accounts VALUES
(4,"David",1000.00,"Noida");

SELECT * FROM accounts;

-- INDEX --
CREATE INDEX idx_branch ON accounts(BRANCH);
SHOW INDEX FROM accounts;

-- It will become way more faster 
SELECT * 
FROM accounts
WHERE branch= "Mumbai";

DROP INDEX idx_branch ON accounts;

-- Composite Index --
CREATE INDEX idx2 ON accounts(BRANCH, balance);
SHOW INDEX FROM accounts;
