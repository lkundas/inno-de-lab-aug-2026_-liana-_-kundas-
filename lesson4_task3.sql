-- 3. Тест 1 (выполняется под hr_user): Успешное чтение данных
SELECT * FROM Employees;
-- 3. Тест 2 (выполняется под hr_user): Попытка INSERT (должна быть ошибка доступа)
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES ('Test', 'User', 'HR', 50000.00);
select current_user;
SELECT current_user;
SELECT current_database();
-- 3. Тест 3 (выполняется под hr_user): Попытка INSERT и UPDATE
UPDATE Employees 
SET Salary = 55000.00 
WHERE FirstName = 'Test';
-- Выдача дополнительных прав на последовательность для успешного INSERT
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;
