from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

import pandas as pd
from sqlalchemy import text


load_dotenv()


def load_to_database(df, table_name):
    """
    Load dataframe into PostgreSQL table
    """

    try:

        database_url = os.getenv("DATABASE_URL")

        engine = create_engine(database_url)

        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        print(f"{table_name} loaded successfully ✅")


    except Exception as e:

        print(f"Error loading {table_name}: {e}")
        


def get_dimension_keys(table_name, id_column, key_column):

    database_url = os.getenv("DATABASE_URL")

    engine = create_engine(database_url)


    query = text(
        f"""
        SELECT 
            {id_column},
            {key_column}
        FROM {table_name}
        """
    )


    with engine.connect() as connection:

        result = connection.execute(query)

        df = pd.DataFrame(
            result.fetchall(),
            columns=result.keys()
        )


    return df