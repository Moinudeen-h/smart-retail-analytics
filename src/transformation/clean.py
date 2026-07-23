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