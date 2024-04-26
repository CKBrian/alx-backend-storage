-- creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Drop trigger
DROP TRIGGER IF EXISTS after_email_change ;

DELIMITER $$

-- New trigger
CREATE TRIGGER after_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$

DELIMITER ;
