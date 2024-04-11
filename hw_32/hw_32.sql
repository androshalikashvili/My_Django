-- Active: 1712586008240@@127.0.0.1@3307@it_step

CREATE TABLE Author (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    AuthorName VARCHAR (25) NOT NULL,
    AuthorLastname VARCHAR (50)
    );


CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    BookName VARCHAR(50),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Author(ID)
);

INSERT INTO Author (`AuthorName`, `AuthorLastname`)
VALUES ('John', 'Smith'), 
('Emily', 'Johnson'), 
('Michael', 'Williams'),
('Sarah', 'Brown'),
('David', 'Jones')
;

INSERT INTO Books (`BookName`, `AuthorID`)
VALUES ("The Secret Garden", 1),
("To Kill a Mockingbird", 2),
("Harry Potter and the Philosopher's Stone", 3),
("1984", 4),
("The Catcher in the Rye", 5)
;

UPDATE books SET `BookName` = "The Great Gatsby" WHERE `BookID` = 3;

SELECT * FROM author;

SELECT * FROM books;

DELETE FROM books;

DELETE FROM author;

DROP TABLE IF EXISTS author, books;
