-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- If the table already exists, your script should not fail
-- Your script can be executed on any database
-- creates a table users with these attributes:
CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
