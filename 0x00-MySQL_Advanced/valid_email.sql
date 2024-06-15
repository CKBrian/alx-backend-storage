-- creates a trigger that resets the attribute valid_email only when the email has been changed.

-- sample outputs:
/*
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
*/
/*
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";
*/
/*
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
-- UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 
*/
-- syntax
-- definer clause CREATE TRIGGER creates new trigger obj
-- trigger name
-- trigger time trigger event
-- trigger body
-- trigger time { BEFORE | AFTER } 
-- trigger event { INSERT | UPDATE | DELETE }
DROP TRIGGER IF EXISTS after_email_change;

DELIMITER $$

CREATE TRIGGER after_email_change
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	SELECT * FROM users;
	IF OLD.email != NEW.email THEN
		UPDATE users SET valid_email = 0 WHERE id = NEW.id;
	END IF;
END$$

DELIMITER ;

