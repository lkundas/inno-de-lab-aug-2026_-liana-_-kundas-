-- 1. Вставить двух новых сотрудников в таблицу Employees (не 'IT')
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Michael', 'Scott', 'Management', 85000.00),
('Pam', 'Beesley', 'Sales', 48000.00);

-- 2. Выбрать всех сотрудников из таблицы Employees
SELECT * FROM Employees;

-- 3. Выбрать только FirstName и LastName сотрудников из отдела 'IT'
SELECT FirstName, LastName 
FROM Employees 
WHERE Department = 'IT';

-- 4. Обновить Salary 'Alice Smith' до 65000.00
UPDATE Employees 
SET Salary = 65000.00 
WHERE FirstName = 'Alice' AND LastName = 'Smith';

-- 5. Удалить сотрудника 'Eve Davis'
DELETE FROM Employees 
WHERE FirstName = 'Eve' AND LastName = 'Davis';

-- 6. Проверить все изменения в таблице
SELECT * FROM Employees;