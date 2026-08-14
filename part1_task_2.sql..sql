 -- Part 1, Task 2: Заказы с суммой больше 1000
SELECT 
    order_id, 
    item, 
    amount, 
    customer_id
FROM Orders
WHERE amount > 1000;
