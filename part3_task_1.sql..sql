SELECT 
    country, 
    COUNT(*)
FROM Customers
GROUP BY country;