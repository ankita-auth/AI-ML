USE instagram;

CREATE TABLE user(
id INT /*PRIMARY KEY*/,
age INT ,
name VARCHAR(30) NOT NULL,
email VARCHAR(50) UNIQUE,
followers INT  DEFAULT 0 ,
following INT,
CONSTRAINT age_check CHECK(age>=13),
PRIMARY KEY(id)

);

create table post(
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);