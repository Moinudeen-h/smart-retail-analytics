import pandas as pd


def clean_products(df):

    df = df.copy()

    # Remove duplicate products
    df = df.drop_duplicates()

    # Convert price to numeric
    df["price"] = pd.to_numeric(
        df["price"]
    )

    return df