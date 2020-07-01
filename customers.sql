--
-- 
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: customer_customer
DROP TABLE IF EXISTS customer_customer;
CREATE TABLE customer_customer(id integer NOT NULL PRIMARY KEY AUTOINCREMENT, full_name varchar (50) NOT NULL, email varchar (10) NOT NULL, date_of_birth date NOT NULL, address varchar (50) NOT NULL);
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (1, 'Okwe Aigbe', 'okweai@gmail.com', '2000-12-15', '123 Verney Park Road, Buckingham');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (2, 'John Sunbi', 'johnsun@gmail.com', '2001-11-18', '3000 Chados Road, Aylesbury');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (3, 'Myriam Jub', 'myriamju@gmail.com', '1999-10-10', '140 Quainton Park Road, Milton Keynes');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (4, 'Jasmine Tes', 'jastes@gmail.com', '2000-04-12', '123 Hyde Park Road, London');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (5, 'Laureen Rufaro', 'laufar@gmail.com', '2002-07-13', '78 Westminster Park Road, London');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (6, 'Tawa Ose', 'Tawaose@gmail.com', '1998-01-21', '500 Launton Park Road, Oxford');
INSERT INTO customer_customer (id, full_name, email, date_of_birth, address) VALUES (7, 'Ose Zech', 'osezech@gmail.com', '1997-12-28', '1 Manchester Park Road, Manchester');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
