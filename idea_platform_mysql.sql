
CREATE DATABASE IF NOT EXISTS idea_platform;
USE idea_platform;

CREATE TABLE students(
    student_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(150),
    year INT,
    university VARCHAR(150)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE innovations(
    idea_id VARCHAR(10) PRIMARY KEY,
    student_id VARCHAR(10),
    idea_title VARCHAR(200),
    category VARCHAR(100),
    submission_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE investors(
    investor_id VARCHAR(10) PRIMARY KEY,
    company VARCHAR(150),
    contact_name VARCHAR(100),
    email VARCHAR(150),
    investment_area VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Advanced Queries
-- 1. List students and the number of projects they've submitted
SELECT s.name, COUNT(i.idea_id) AS projects_submitted
FROM students s
LEFT JOIN innovations i ON s.student_id = i.student_id
GROUP BY s.name
ORDER BY projects_submitted DESC;

-- 2. Projects count by category
SELECT category, COUNT(idea_id) AS total_projects
FROM innovations
GROUP BY category
HAVING total_projects > 5
ORDER BY total_projects DESC;

-- 3. Projects count by status
SELECT status, COUNT(idea_id) AS projects_count
FROM innovations
GROUP BY status;

-- Stored procedure for updating project status
DELIMITER //
CREATE PROCEDURE update_project_status(IN project_id VARCHAR(10), IN new_status VARCHAR(50))
BEGIN
    UPDATE innovations
    SET status = new_status
    WHERE idea_id = project_id;
END//
DELIMITER ;
