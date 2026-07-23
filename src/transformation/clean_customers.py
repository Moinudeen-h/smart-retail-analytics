import pandas as pd


def clean_customers(df):
    """
    Clean customer data before loading into database
    """

    # Create a copy to avoid modifying original data
    df = df.copy()

    # Remove duplicate customers
    df = df.drop_duplicates()

    # Handle missing age values
    df["age"] = df["age"].fillna(df["age"].mean())

    # Convert age to integer
    df["age"] = df["age"].astype(int)

    # Convert date column to datetime format
    df["registration_date"] = pd.to_datetime(
        df["registration_date"]
    )

    return df


if __name__ == "__main__":

    customers = pd.read_csv(
        "data/raw/customers.csv"
    )

    cleaned_customers = clean_customers(customers)

    print(cleaned_customers)

    print("\nData information:")
    print(cleaned_customers.info())