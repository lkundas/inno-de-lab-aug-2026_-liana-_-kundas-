-- 1. Создание функции CalculateAnnualBonus (с использованием PL/pgSQL)
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(employee_id INT, Salary DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
    RETURN Salary * 0.10;
END;
$$ LANGUAGE plpgsql;
-- 2. Использование этой функции в операторе SELECT для каждого сотрудника
SELECT 
    EmployeeID, 
    FirstName, 
    LastName, 
    Salary, 
    CalculateAnnualBonus(EmployeeID, Salary) AS AnnualBonus
FROM Employees;
-- 3. Создание представления (View) IT_Department_View
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'IT';
-- 4. Выборка данных из созданного представления
SELECT * FROM IT_Department_View;