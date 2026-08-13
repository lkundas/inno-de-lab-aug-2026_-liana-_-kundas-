-- Part 2, Task 2: Список доставок со статусом и именами клиентов
SELECT 
    s.status, 
    c.first_name, 
    c.last_name
FROM Shippings s
JOIN Customers c ON s.customer = c.customer_id;
