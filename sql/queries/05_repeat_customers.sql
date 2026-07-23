SELECT
    c.customer_name,
    COUNT(f.sale_id) AS total_orders
FROM fact_sales f
JOIN dim_customers c
ON f.customer_key = c.customer_key
GROUP BY
    c.customer_name
HAVING COUNT(f.sale_id) > 1
ORDER BY
    total_orders DESC;