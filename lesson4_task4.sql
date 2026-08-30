-- 1. Увеличить Salary всех сотрудников в отделе 'HR' на 10%.
UPDATE Employees 
SET Salary = Salary * 1.10 
WHERE Department = 'HR';
-- 2. Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'.
UPDATE Employees 
SET Department = 'Senior IT' 
WHERE Salary > 70000.00;
-- 3. Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects.
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID SERIAL PRIMARY KEY,
    ProjectName VARCHAR(100) NOT NULL,
    Budget DECIMAL(12, 2),
    StartDate DATE,
    EndDate DATE
);

CREATE TABLE IF NOT EXISTS EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    HoursWorked INT,
    PRIMARY KEY (EmployeeID, ProjectID)
);

INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) VALUES
('Website Redesign', 150000.00, '2023-01-15', '2023-06-30'),
('Mobile App Development', 200000.00, '2023-03-01', '2023-10-31'),
('Internal Tools Upgrade', 80000.00, '2023-05-10', '2023-09-15')
ON CONFLICT DO NOTHING;

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked) VALUES
(2, 1, 160),
(4, 1, 120),
(2, 2, 200),
(1, 3, 80),
(3, 3, 100)
ON CONFLICT DO NOTHING;
-- 3. Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects.
DELETE FROM Employees 
WHERE EmployeeID NOT IN (
    SELECT EmployeeID 
    FROM EmployeeProjects
);
-- 4. В рамках одной транзакции вставить новый проект и назначить на него двух существующих сотрудников (например, с ID 1 и 2) с указанным количеством HoursWorked.
BEGIN;

WITH inserted_project AS (
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('Cloud Migration', 250000.00, '2026-09-01', '2027-03-01')
    RETURNING ProjectID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT e.EmployeeID, np.ProjectID, 120
FROM Employees e, inserted_project np
WHERE e.EmployeeID IN (1, 2);

COMMIT;