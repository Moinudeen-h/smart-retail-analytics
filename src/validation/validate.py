import pandas as pd


def validate_customers(df):

    errors = []

    # Check required columns
    required_columns = [
        "customer_id",
        "customer_name",
        "age"
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(
                f"Missing column: {column}"
            )


    # Check missing customer IDs
    if df["customer_id"].isnull().any():
        errors.append(
            "Customer ID contains missing values"
        )


    # Check duplicate customer IDs
    if df["customer_id"].duplicated().any():
        errors.append(
            "Duplicate customer IDs found"
        )


    # Check age range
    if (df["age"] < 0).any():
        errors.append(
            "Invalid age detected"
        )


    if len(errors) == 0:
        print("Validation passed ✅")
        return True

    else:
        print("Validation failed ❌")

        for error in errors:
            print(error)

        return False



if __name__ == "__main__":

    customers = pd.read_csv(
        "data/raw/customers.csv"
    )

    validate_customers(customers)