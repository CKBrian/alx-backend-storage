-- creates a stored procedure AddBonus that adds a new correction for a student.

--  Procedure name AddBonus with 3 inputs :
--  user_id, a users.id value (user_id is linked to an existing users)
--  project_id, a new or already exists projects - if no projects.name found in the table, creates it
--  score, the score value for the correction

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus (
		IN user_id  INT,
		IN project_name  VARCHAR(255),
		IN score  INT)
BEGIN
	DECLARE new_project_id INT DEFAULT 0;
	SELECT id INTO new_project_id FROM projects WHERE name = project_name LIMIT 1;
	IF new_project_id > 0 THEN
		INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, new_project_id, score);
	ELSE
		INSERT INTO projects(name) VALUES (project_name);
		SELECT LAST_INSERT_ID() INTO new_project_id;
		INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, new_project_id, score);
		
	END IF;
COMMIT;
END$$

DELIMITER ;
