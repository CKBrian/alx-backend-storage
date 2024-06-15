-- create user for the project
CREATE USER IF NOT EXISTS 'brian'@'localhost' IDENTIFIED BY 'password';
-- Grants all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'brian'@'localhost';
FLUSH PRIVILEGES;
