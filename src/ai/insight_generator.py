from src.ai.llm_client import ask_llm


def generate_insight(question, result):

    prompt = f"""

You are a business intelligence analyst working for a Sri Lankan retail company.

All monetary values in the database are in Sri Lankan Rupees (LKR).

Rules:
- Never use dollar signs ($).
- Always use LKR when mentioning money.
- Keep explanations suitable for business executives.

Based on the question and database result below,
provide a simple executive summary.

Question:
{question}

Result:
{result}

Explain:
- What happened based only on the provided data
- Why this insight is useful for business decisions
- One recommendation supported by the data

Do not assume causes that are not present in the data.
Do not invent customer behaviour explanations.

Keep it concise.

"""

    return ask_llm(prompt)