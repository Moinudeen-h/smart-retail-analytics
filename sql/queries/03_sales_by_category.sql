SELECT
    p.category,
    SUM(f.sales_amount) AS total_sales
FROM fact_sales f
JOIN dim_products p
ON f.product_key = p.product_key
GROUP BY
    p.category
ORDER BY
    total_sales DESC;