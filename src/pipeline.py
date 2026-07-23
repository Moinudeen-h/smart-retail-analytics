from pathlib import Path

from src.data_ingestion.extract import load_csv

from src.transformation.clean import (
    clean_customers,
    clean_products,
    clean_sales,
    prepare_sales_fact,
    prepare_date_dimension
)

from src.validation.validate import (
    validate_customers,
    validate_products,
    validate_sales
)

from src.database.loader import (
    load_to_database,
    get_dimension_keys
)


# -------------------------
# Customers Pipeline
# -------------------------

customers = load_csv(
    Path("data/raw/customers.csv")
)

customers = clean_customers(customers)

if validate_customers(customers):

    load_to_database(
        customers,
        "dim_customers"
    )


# -------------------------
# Products Pipeline
# -------------------------

products = load_csv(
    Path("data/raw/products.csv")
)

products = clean_products(products)

if validate_products(products):

    load_to_database(
        products,
        "dim_products"
    )


# -------------------------
# Get Warehouse Keys
# -------------------------

customer_keys = get_dimension_keys(
    "dim_customers",
    "customer_id",
    "customer_key"
)


product_keys = get_dimension_keys(
    "dim_products",
    "product_id",
    "product_key"
)


# -------------------------
# Sales & Date Pipeline
# -------------------------

sales = load_csv(
    Path("data/raw/sales.csv")
)

sales = clean_sales(sales)

# 1. Create and load the date dimension while 'sale_date' still exists in sales
date_dimension = prepare_date_dimension(
    sales
)

load_to_database(
    date_dimension,
    "dim_date"
)

# 2. Prepare the sales fact table (which converts and drops 'sale_date')
sales_fact = prepare_sales_fact(
    sales,
    customer_keys,
    product_keys
)

# 3. Validate and load the fact table into the database
if validate_sales(sales_fact):
    load_to_database(
        sales_fact,
        "fact_sales"
    )