from sqlalchemy import text
from src.database.loader import engine


def execute_sql(query):
    """
    Execute generated SQL query on PostgreSQL database
    """

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text(query)
            )

            rows = result.fetchall()

            columns = result.keys()

            return {
                "columns": list(columns),
                "data": [list(row) for row in rows]
            }

    except Exception as e:

        return {
            "error": str(e)
        }