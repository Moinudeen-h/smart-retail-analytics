import pandas as pd


def clean_customers(df):
    """
    Clean customer dimension data
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing age values
    if "age" in df.columns:
        df["age"] = df["age"].fillna(
            df["age"].median()
        )

    # Convert registration date
    if "registration_date" in df.columns:
        df["registration_date"] = pd.to_datetime(
            df["registration_date"]
        )

    # Remove leading/trailing spaces
    string_columns = df.select_dtypes(
        include="object"
    ).columns

    for col in string_columns:
        df[col] = df[col].str.strip()

    return df



def clean_products(df):
    """
    Clean product dimension data
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove spaces
    string_columns = df.select_dtypes(
        include="object"
    ).columns

    for col in string_columns:
        df[col] = df[col].str.strip()

    # Convert price column
    if "price" in df.columns:
        df["price"] = pd.to_numeric(
            df["price"],
            errors="coerce"
        )

        # Fill missing prices with median
        df["price"] = df["price"].fillna(
            df["price"].median()
        )

    return df



def clean_sales(df):
    """
    Clean sales transaction data
    """

    df = df.copy()

    # Remove duplicate transactions
    df = df.drop_duplicates()

    # Remove spaces
    string_columns = df.select_dtypes(
        include="object"
    ).columns

    for col in string_columns:
        df[col] = df[col].str.strip()

    # Convert date column
    if "sale_date" in df.columns:
        df["sale_date"] = pd.to_datetime(
            df["sale_date"]
        )

    # Handle numerical missing values
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(0)

    # Calculate sales amount

    if all(col in df.columns for col in ["quantity", "unit_price", "discount"]):

        df["sales_amount"] = (
            df["quantity"] * df["unit_price"]
            - df["discount"]
        )

    return df



def clean_date(df):
    """
    Clean date dimension data
    """

    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date format
    if "full_date" in df.columns:
        df["full_date"] = pd.to_datetime(
            df["full_date"]
        )

    return df

def prepare_sales_fact(
    sales,
    customers,
    products
):
    """
    Convert sales transaction data
    into warehouse fact table format
    """

    sales = sales.copy()

    # Map customer IDs to customer keys

    sales = sales.merge(
        customers[
            [
                "customer_id",
                "customer_key"
            ]
        ],
        on="customer_id",
        how="left"
    )


    # Map product IDs to product keys

    sales = sales.merge(
        products[
            [
                "product_id",
                "product_key"
            ]
        ],
        on="product_id",
        how="left"
    )


    # Remove original IDs

    sales.drop(
        columns=[
            "customer_id",
            "product_id"
        ],
        inplace=True
    )
    
    sales["date_key"] = (
        sales["sale_date"]
        .dt.strftime("%Y%m%d")
        .astype(int)
    )


    sales.drop(
        columns=["sale_date"],
        inplace=True
    )

    return sales

def prepare_date_dimension(sales):

    dates = sales[["sale_date"]].drop_duplicates()

    dates["full_date"] = dates["sale_date"]

    dates["date_key"] = (
        dates["full_date"]
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    dates["day"] = dates["full_date"].dt.day

    dates["month"] = dates["full_date"].dt.month

    dates["month_name"] = (
        dates["full_date"]
        .dt.month_name()
    )

    dates["quarter"] = (
        "Q" +
        dates["full_date"]
        .dt.quarter
        .astype(str)
    )

    dates["year"] = (
        dates["full_date"]
        .dt.year
    )

    dates["weekday"] = (
        dates["full_date"]
        .dt.day_name()
    )


    dates.drop(
        columns=["sale_date"],
        inplace=True
    )


    return dates