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
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "raw"

def run_pipeline():

    # -------------------------
    # Customers Pipeline
    # -------------------------

    customers = load_csv(
        DATA_PATH / "customers.csv"
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
        DATA_PATH / "products.csv"
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
        DATA_PATH / "sales.csv"
    )

    sales = clean_sales(sales)


    # Create Date Dimension

    date_dimension = prepare_date_dimension(
        sales
    )

    load_to_database(
        date_dimension,
        "dim_date"
    )


    # Prepare Fact Table

    sales_fact = prepare_sales_fact(
        sales,
        customer_keys,
        product_keys
    )


    # Validate and Load Fact Table

    if validate_sales(sales_fact):

        load_to_database(
            sales_fact,
            "fact_sales"
        )


    print("Retail ETL Pipeline completed successfully ✅")


# Keep normal Python execution working

if __name__ == "__main__":
    run_pipeline()