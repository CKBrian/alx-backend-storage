-- Drops the proceduree if it exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- computes and stores the average score for a student from the corrections.score table

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE user_average DECIMAL(5, 2) DEFAULT 0;

    -- Get average score using AVG and store INTO a variable
    SELECT AVG(corrections.score) INTO user_average FROM corrections WHERE corrections.user_id = user_id;
    -- store the result into a users.average_score 
    UPDATE users SET average_score = user_average WHERE id = user_id;
COMMIT;
END$$

DELIMITER ;