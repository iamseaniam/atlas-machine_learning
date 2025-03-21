-- creates a trigger that resets the attribute valid_email
DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END;

//

DELIMITER ;
