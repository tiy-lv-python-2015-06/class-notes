#Student table
CREATE TABLE public.student (
  id SERIAL PRIMARY KEY NOT NULL, 
  name CHARACTER VARYING(50) NOT NULL,
  email CHARACTER VARYING(50) NOT NULL,
  address INTEGER
);

#Address Table
CREATE TABLE public.address (
  id SERIAL PRIMARY KEY NOT NULL,
  city CHARACTER VARYING(25) NOT NULL,
  state CHARACTER VARYING(20) NOT NULL,
  zip INTEGER NOT NULL
);

#Insert some values into our tables
INSERT INTO student (name, email, address) VALUES ('Frodo Baggins', 'frodo@theshire.com', 0);
INSERT INTO student (name, email, address) VALUES ('Samwise', 'sam@theshire.com', 0);
INSERT INTO student (name, email, address) VALUES ('Gandalf', 'gandalf@wizards.gov', 0);
INSERT INTO student (name, email, address) VALUES ('Saruman', 'saruman@wizards.gov', 0);
INSERT INTO address (city, state, zip) VALUES ('Hobbiton', 'The Shire', 12445);
INSERT INTO address (city, state, zip) VALUES ('Orthanc', 'Isengard', 98765);
INSERT INTO address (city, state, zip) VALUES ('Minis Tirith', 'Gondor', 55555);

#Simple Selects
select * from student where id > 2;
select * from address where id = 2;

#Inner join returns only rows that match in each table
SELECT student.id FROM student INNER JOIN address ON student.address = address.id;

#Left join returns all rows in the first table and nulls the second table columns if no match
SELECT * FROM student LEFT JOIN address ON student.address = address.id;

#Right join returns all rows in the second table and returns null columns for non-matching rows in the first table
SELECT * FROM student RIGHT JOIN address ON student.address = address.id;

#Outer Join returns all rows from each table and just leaves non-matching fields as null
SELECT * FROM student FULL OUTER JOIN address ON student.address = address.id;

#Group by aggregates allowing for sum(), count() etc  All fields names must be unique or an aggregate like below
select city, state, zip, name, count(*)
  FROM address
    JOIN student on address.id = student.address
  GROUP BY address.id;
