  -- Part 7, Task 1: Клиенты с >=2 заказами и доставкой 'Delivered'
SELECT 
    c.first_name || ' ' ||  c.last_name AS full_name,
    c.country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE c.customer_id IN (
    SELECT customer 
    FROM Shippings 
    WHERE status = 'Delivered'
)
GROUP BY c.customer_id, c.first_name, c.last_name, c.country
HAVING COUNT(o.order_id) >= 2;
