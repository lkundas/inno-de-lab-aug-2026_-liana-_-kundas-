-- Выдача дополнительных прав на последовательность для успешного INSERT
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;
-- 3. Тест 1 (выполняется под hr_user): Успешное чтение данных
SELECT * FROM Employees;
-- 3. Тест 2 (выполняется под hr_user): Попытка INSERT (должна быть ошибка доступа)
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES ('Test', 'User', 'HR', 50000.00);
SELECT current_user;
SELECT current_database();
-- 3. Тест 3 (выполняется под hr_user): Проверка INSERT и UPDATE
-- Сначала проверяем INSERT:
INSERT INTO Employees (FirstName, LastName, Department, Salary) 
VALUES ('Test', 'User', 'HR', 50000.00);

-- Затем проверяем UPDATE:
UPDATE Employees 
SET Salary = 55000.00 
WHERE FirstName = 'Test';
