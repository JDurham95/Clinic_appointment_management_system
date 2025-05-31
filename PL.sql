/**
PL Step 5 Draft
Fidella Wu, Jacob Durham
CS340 Introduction to Databases


Citations:
Citation for Stored Procedures
    Originality: Adapted
    Date: 5/17/2025
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-pl-slash-sql-part-2-stored-procedures-for-cud?module_item_id=25352959
    Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968


**/


-- #############################
-- CREATE clinic
-- #############################
DROP PROCEDURE IF EXISTS sp_insert_clinic;


DELIMITER //
CREATE PROCEDURE sp_insert_clinic(
    IN p_address varchar(45),
    IN p_city varchar(45),
    IN p_state varchar(2),
    IN p_postalCode varchar(5),
    IN p_phoneNumber char(12),
    OUT p_id INT)
BEGIN
    INSERT INTO `Clinics` (`address`, `city`, `state`, `postalCode`, `phoneNumber`)
    VALUES (p_address, p_city, p_state, p_postalCode, p_phoneNumber);


    -- Store the ID of the last inserted row
    SELECT LAST_INSERT_ID() into p_id;
    -- Display the ID of the last inserted clinic
    SELECT LAST_INSERT_ID() AS 'new_id';
END //
DELIMITER ;


-- #############################
-- CREATE patient
-- #############################
DROP PROCEDURE IF EXISTS sp_insert_patient;


DELIMITER //
CREATE PROCEDURE sp_insert_patient(
    IN p_firstName varchar(45),
    IN p_lastName varchar(45),
    IN p_phoneNumber char(12),
    IN p_email varchar(150),
    IN p_dateOfBirth DATE,
    IN p_gender varchar(10),
    IN p_clinicId INT,
    OUT p_id INT)
BEGIN
    INSERT INTO `Patients` (`firstName`, `lastName`, `phoneNumber`, `email`, `dateOfBirth`, `gender`, `clinicId`)
    VALUES (p_firstName, p_lastName, p_phoneNumber, p_email, p_dateOfBirth, p_gender, p_clinicId);


    -- Store the ID of the last inserted row
    SELECT LAST_INSERT_ID() into p_id;
    -- Display the ID of the last inserted patient
    SELECT LAST_INSERT_ID() AS 'new_id';
END //
DELIMITER ;


-- #############################
-- CREATE appointment
-- #############################
DROP PROCEDURE IF EXISTS sp_insert_appointment;


DELIMITER //
CREATE PROCEDURE sp_insert_appointment(
    IN p_dateTime DATETIME,
    IN p_clinicId INT,
    IN p_patientId INT,
    IN p_statusId INT,
    OUT p_id INT)
BEGIN
    INSERT INTO `Appointments` (`dateTime`, `clinicId`,`patientId`,`statusId`)
    VALUES(p_dateTime, p_clinicId, p_patientId, p_statusId);


    -- Store the ID of the last inserted row
    SELECT LAST_INSERT_ID() into p_id;
    -- Display the ID of the last inserted appointment
    SELECT LAST_INSERT_ID() AS 'new_id';
END //
DELIMITER ;


-- #############################
-- CREATE appointmenttest
-- #############################
DROP PROCEDURE IF EXISTS sp_insert_appointmenttest;


DELIMITER //
CREATE PROCEDURE sp_insert_appointmenttest(
    IN p_appointmentId INT,
    IN p_testId INT,
    IN p_testResultId INT,
    OUT p_id INT)
BEGIN
    INSERT INTO `AppointmentsTests` (`appointmentId`, `testId`, `testResultId`)
    VALUES (p_appointmentId, p_testId, p_testResultId);


    -- Store the ID of the last inserted row
    SELECT LAST_INSERT_ID() into p_id;
    -- Display the ID of the last inserted appointmentTest
    SELECT LAST_INSERT_ID() AS 'new_id';
END //
DELIMITER ;


-- #############################
-- CREATE test
-- #############################
DROP PROCEDURE IF EXISTS sp_insert_test;


DELIMITER //
CREATE PROCEDURE sp_insert_test(
    IN p_name VARCHAR(45),
    OUT p_id INT)
BEGIN
    INSERT INTO `Tests` (`name`)
    VALUES (p_name);


    -- Store the ID of the last inserted row
    SELECT LAST_INSERT_ID() into p_id;
    -- Display the ID of the last inserted appointmentTest
    SELECT LAST_INSERT_ID() AS 'new_id';
END //
DELIMITER ;
-- ###################
-- DELETE Tests
-- ####################
DROP PROCEDURE IF EXISTS sp_delete_test;
DELIMITER //
CREATE PROCEDURE sp_delete_test(IN p_testId INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;
    START TRANSACTION;
        DELETE FROM `Tests` WHERE `testId` = p_testId;
        IF ROW_COUNT() =0 THEN
            SET error_message = CONCAT('No matching record found in Tests for testId:', p_testId);
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
        END IF;
    COMMIT;
END //
DELIMITER ;
-- ###################
-- DELETE Clinics
-- ####################
DROP PROCEDURE IF EXISTS sp_delete_clinic;
DELIMITER //
CREATE PROCEDURE sp_delete_clinic(IN p_clinicId INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;
    START TRANSACTION;
        DELETE FROM `Clinics` WHERE `clinicId` = p_clinicId;
        IF ROW_COUNT() =0 THEN
            SET error_message = CONCAT('No matching record found in Clinics for clinicId:', p_clinicId);
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
        END IF;
    COMMIT;
END //
DELIMITER ;


-- ####################
-- DELETE Appointments
-- ####################
DROP PROCEDURE IF EXISTS sp_delete_appointment;
DELIMITER / /


CREATE PROCEDURE sp_delete_appointment(IN p_appointmentId INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;
    START TRANSACTION;
        DELETE FROM `Appointments` WHERE `appointmentId` = p_appointmentId;
        IF ROW_COUNT() =0 THEN
            SET error_message = CONCAT('No matching record found in Appointments for appointmentId:', p_appointmentId);
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
        END IF;
    COMMIT;
END//
DELIMITER ;


-- ###################
-- UPDATE Patients
-- ####################
DROP PROCEDURE IF EXISTS sp_update_patient;
DELIMITER / /
CREATE PROCEDURE `sp_update_patient`(IN p_patientId INT,
    IN p_firstName VARCHAR(45),
    IN p_lastName VARCHAR(45),
    IN p_phoneNumber char(12),
    IN p_email VARCHAR(150),
    IN p_dateOfBirth DATE,
    IN p_gender ENUM('Male', 'Female', 'Unknown'),
    IN p_clinicId INT  )
BEGIN
    UPDATE `Patients`
    SET `firstName` = p_firstName,
    `lastName` = p_lastName,
    `phoneNumber` = p_phoneNumber,
    `email` = p_email,
    `dateOfBirth` = p_dateOfBirth,
    `gender` = p_gender,
    `clinicId` = p_clinicId
    WHERE `patientId` = p_patientId;
END / /
DELIMITER ;


-- ###################
-- UPDATE Tests
-- ####################
DROP PROCEDURE IF EXISTS sp_update_test;
DELIMITER / /
CREATE PROCEDURE `sp_update_test`(
    IN p_testId INT,
    IN p_name VARCHAR(45))
BEGIN
    UPDATE `Tests`
    SET `name` = p_name
    WHERE `testId` = p_testId;
END / /
DELIMITER ;
-- ###################
-- UPDATE Clinics
-- ####################
DROP PROCEDURE IF EXISTS sp_update_clinic;
DELIMITER / /
CREATE PROCEDURE `sp_update_clinic`(
    IN p_clinicId INT,
    IN p_address VARCHAR(45),
    IN p_city VARCHAR(45),
    IN p_state CHAR(2),
    IN p_postalCode VARCHAR(5),
    IN p_phoneNumber CHAR(12))
BEGIN
    UPDATE `Clinics`
    SET `address` = p_address,
    `city` = p_city,
    `state` = p_state,
    `postalCode` = p_postalCode,
    `phoneNumber`= p_phoneNumber
    WHERE `clinicId` = p_clinicId;
END / /
DELIMITER ;


-- ###################
-- UPDATE Appointments
-- ####################
DROP PROCEDURE IF EXISTS sp_update_appointment;
DELIMITER / /
CREATE PROCEDURE `sp_update_appointment`(
    IN p_appointmentId INT,
    IN p_dateTime DATETIME,
    IN p_clinicId INT,
    IN p_patientId INT,
    IN p_statusId INT
    )
BEGIN
    UPDATE `Appointments`
    SET `dateTime` = p_dateTime,
    `clinicId` = p_clinicId,
    `patientId`= p_patientId,
    `statusId` = p_statusId
    WHERE `appointmentId` = p_appointmentId;
END / /
DELIMITER ;


-- ###################
-- UPDATE AppointmentsTests
-- ####################
DROP PROCEDURE IF EXISTS sp_update_appointmenttest;
DELIMITER / /
CREATE PROCEDURE `sp_update_appointmenttest`(
    IN p_appointmentTestId INT,
    IN p_appointmentId INT,
    IN p_testId INT,
    IN p_testResultId INT
    )
BEGIN
    UPDATE `AppointmentsTests`
    SET `appointmentId` = p_appointmentId,
    `testId` = p_testId,
    `testResultId`= p_testResultId
    WHERE `appointmentTestId` = p_appointmentTestId;
END / /
DELIMITER ;


-- ###################
-- UPDATE Statuses
-- ####################
DROP PROCEDURE IF EXISTS sp_update_status;
DELIMITER / /
CREATE PROCEDURE `sp_update_status`(
    IN p_statusId INT,
    IN p_status VARCHAR(45))
BEGIN
    UPDATE `Statuses`
    SET `status` = p_status
    WHERE `statusId` = p_statusid;
END / /
DELIMITER ;


-- ###################
-- UPDATE Results
-- ####################
DROP PROCEDURE IF EXISTS sp_update_result;
DELIMITER / /
CREATE PROCEDURE `sp_update_result`(
    IN p_resultId INT,
    IN p_result VARCHAR(45))
BEGIN
    UPDATE `Results`
    SET `result` = p_result
    WHERE `testResultId` = p_resultId;
END / /
DELIMITER ;



