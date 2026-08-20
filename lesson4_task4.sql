-- 1. Увеличить Salary всех сотрудников в отделе 'HR' на 10%.
UPDATE Employees 
SET Salary = Salary * 1.10 
WHERE Department = 'HR';
-- 2. Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'.
UPDATE Employees 
SET Department = 'Senior IT' 
WHERE Salary > 70000.00;
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
