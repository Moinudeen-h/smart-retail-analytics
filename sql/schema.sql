CREATE TABLE dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) UNIQUE NOT NULL,
    customer_name VARCHAR(100),
    gender VARCHAR(20),
    age INTEGER,
    city VARCHAR(50),
    country VARCHAR(50),
    registration_date DATE
);

CREATE TABLE dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    supplier VARCHAR(100)
);


CREATE TABLE fact_sales (
    sale_key SERIAL PRIMARY KEY,
    sale_id VARCHAR(50) UNIQUE NOT NULL,

    customer_key INTEGER REFERENCES dim_customers(customer_key),
    product_key INTEGER REFERENCES dim_products(product_key),

    date_key INTEGER REFERENCES dim_date(date_key),

    quantity INTEGER,
    unit_price DECIMAL(10,2),
    discount DECIMAL(10,2),

    sales_amount DECIMAL(12,2)
);