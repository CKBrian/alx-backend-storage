-- 10-div.sql
-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

DELIMITER $$

CREATE FUNCTION SafeDiv(a INTEGER, b INTEGER) RETURNS FLOAT
NO SQL
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END$$

DELIMITER ;
