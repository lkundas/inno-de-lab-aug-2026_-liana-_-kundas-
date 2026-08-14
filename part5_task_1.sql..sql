  -- Part 5, Task 1: Поиск клиентов с максимальной суммой заказа
SELECT 
    c.first_name, 
    c.last_name, 
    o.amount
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
WHERE o.amount = (SELECT MAX(amount) FROM Orders);
