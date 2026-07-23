import pandas as pd
from pathlib import Path


def load_csv(file_path):
    """
    Load CSV file into pandas DataFrame
    """

    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}")

        return df

    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


if __name__ == "__main__":

    customers_path = Path("data/raw/customers.csv")

    customers = load_csv(customers_path)

    if customers is not None:
        print(customers.head())