-- script that creates a stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(5,2);
    
    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    
    -- Update the user's average score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;

//

DELIMITER ;
