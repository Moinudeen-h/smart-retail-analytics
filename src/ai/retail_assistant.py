from src.ai.sql_generator import generate_sql
from src.ai.sql_executor import execute_sql
from src.ai.insight_generator import generate_insight


def ask_retail_ai(question):
    """
    Complete AI analytics workflow:
    Question → SQL → Database → Insight
    """

    print("Generating SQL...")

    sql = generate_sql(question)


    print("Executing SQL...")

    result = execute_sql(sql)


    if "error" in result:
        return {
            "sql": sql,
            "error": result["error"]
        }


    print("Generating business insight...")

    insight = generate_insight(
        question,
        result
    ).replace("**", "")


    return {
        "question": question,
        "sql": sql,
        "result": result,
        "insight": insight
    }