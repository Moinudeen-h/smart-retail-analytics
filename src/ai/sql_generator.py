from src.ai.llm_client import ask_llm
from src.ai.schema_context import DATABASE_SCHEMA


def generate_sql(question):
    """
    Convert natural language question into SQL query
    """

    prompt = f"""

You are an expert SQL developer and data analyst.

Your task is to convert a business question into a PostgreSQL SQL query.

Database schema:

{DATABASE_SCHEMA}


Business Question:

{question}


Instructions:

- Generate only SQL.
- Do not include explanations.
- Do not use markdown code blocks.
- Use correct joins based on the schema.
- Use aggregation when required.

SQL Query:

"""

    sql = ask_llm(prompt)

    return sql.strip()