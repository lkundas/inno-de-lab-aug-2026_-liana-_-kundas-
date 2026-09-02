-- 1. Создать новую таблицу Departments
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

-- 2. Изменить таблицу Employees, добавив новый столбец Email
ALTER TABLE Employees 
ADD COLUMN Email VARCHAR(100);

-- 3. Заполнить столбец Email для всех текущих сотрудников
UPDATE Employees SET Email = 'alice.smith@example.com' WHERE FirstName = 'Alice' AND LastName = 'Smith';
UPDATE Employees SET Email = 'bob.johnson@example.com' WHERE FirstName = 'Bob' AND LastName = 'Johnson';
UPDATE Employees SET Email = 'charlie.brown@example.com' WHERE FirstName = 'Charlie' AND LastName = 'Brown';
UPDATE Employees SET Email = 'diana.prince@example.com' WHERE FirstName = 'Diana' AND LastName = 'Prince';
UPDATE Employees SET Email = 'michael.scott@example.com' WHERE FirstName = 'Michael' AND LastName = 'Scott';
UPDATE Employees SET Email = 'pam.beesley@example.com' WHERE FirstName = 'Pam' AND LastName = 'Beesley';

-- 4. Добавить ограничение UNIQUE к столбцу Email в таблице Employees
ALTER TABLE Employees 
ADD CONSTRAINT unique_employee_email UNIQUE (Email);

-- 5. Переименовать столбец Location в OfficeLocation в таблице Departments
ALTER TABLE Departments 
RENAME COLUMN Location TO OfficeLocation;