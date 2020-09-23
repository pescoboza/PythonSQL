CREATE TABLE colonist(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(32) NOT NULL,
    occupation VARCHAR(32) NOT NULL,
    age INT NOT NULL
);
INSERT INTO colonist
VALUES(1, 'Cauvery', 'Miner', 36);
INSERT INTO colonist
VALUES(2, 'Lilly', 'Botanist', 123);
INSERT INTO colonist
VALUES(3, 'Xavier', 'Arquitect', 46);
INSERT INTO colonist
VALUES(4, 'July', 'Swindler', 26);
INSERT INTO colonist
VALUES(5, 'Borath', 'Thief', 17);
INSERT INTO colonist
VALUES(6, 'Sandana', 'Priestess', 154);
SELECT *
FROM colonist;