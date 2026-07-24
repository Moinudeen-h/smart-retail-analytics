DATABASE_SCHEMA = """

You are working with a PostgreSQL retail analytics warehouse.

The database follows a star schema.

FACT TABLE:

fact_sales
-----------
sale_id
date_key
customer_key
product_key
quantity
unit_price
discount
sales_amount


DIMENSION TABLES:

dim_customers
-------------
customer_key
customer_id
customer_name
gender
age
city
country
registration_date


dim_products
------------
product_key
product_id
product_name
category
price


dim_date
--------
date_key
full_date
year
month
month_name


Relationships:

fact_sales.customer_key 
    joins dim_customers.customer_key

fact_sales.product_key
    joins dim_products.product_key

fact_sales.date_key
    joins dim_date.date_key


Important rules:

- Always use PostgreSQL SQL syntax.
- Always use table aliases.
- Use sales_amount for revenue calculations.
- Never invent columns.
- Return only SQL queries.

"""