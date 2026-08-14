   -- Part 3, Task 2: Общее количество заказов и средняя сумма по каждому товару
SELECT 
    item, 
    COUNT(*) AS count, 
    AVG(amount) AS avg_amount
FROM Orders
GROUP BY item;
