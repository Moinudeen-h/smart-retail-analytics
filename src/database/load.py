import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from src.transformation.clean_customers import clean_customers


load_dotenv()


def load_to_database(df, table_name):

    database_url = os.getenv("DATABASE_URL")

    engine = create_engine(database_url)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded successfully")


if __name__ == "__main__":

    # Extract
    customers = pd.read_csv(
        "data/raw/customers.csv"
    )

    # Transform
    customers_clean = clean_customers(
        customers
    )

    # Load
    load_to_database(
        customers_clean,
        "dim_customers"
    )