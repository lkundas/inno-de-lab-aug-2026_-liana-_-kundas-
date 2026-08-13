 -- Part 3, Task 1: Подсчет количества клиентов в каждой стране
SELECT 
    country, 
    COUNT(*)
FROM Customers
GROUP BY country;
