def validate_customers(df):
    """
    Validate customer dimension data
    """

    checks = {

        "Customer ID exists":
            df["customer_id"].notnull().all(),

        "Customer names exist":
            df["customer_name"].notnull().all(),

        "No duplicate customer IDs":
            df["customer_id"].is_unique,

        "Age values are valid":
            (df["age"] > 0).all()

    }

    return run_checks(checks)



def validate_products(df):
    """
    Validate product dimension data
    """

    checks = {

        "Product ID exists":
            df["product_id"].notnull().all(),

        "Product names exist":
            df["product_name"].notnull().all(),

        "No duplicate product IDs":
            df["product_id"].is_unique,

        "Price is positive":
            (df["price"] >= 0).all()

    }

    return run_checks(checks)



def validate_sales(df):
    """
    Validate sales fact data
    """

    checks = {

        "Sale ID exists":
            df["sale_id"].notnull().all(),

        "Customer key exists":
            df["customer_key"].notnull().all(),

        "Product key exists":
            df["product_key"].notnull().all(),

        "Quantity is positive":
            (df["quantity"] > 0).all(),

        "Sales amount is valid":
            (df["sales_amount"] >= 0).all()

    }

    return run_checks(checks)



def validate_date(df):
    """
    Validate date dimension data
    """

    checks = {

        "Date key exists":
            df["date_key"].notnull().all(),

        "Date values exist":
            df["full_date"].notnull().all(),

        "No duplicate dates":
            df["full_date"].is_unique

    }

    return run_checks(checks)



def run_checks(checks):
    """
    Execute validation checks
    """

    passed = True

    for name, result in checks.items():

        if result:
            print(f"PASS ✅ : {name}")

        else:
            print(f"FAIL ❌ : {name}")
            passed = False


    if passed:
        print("\nAll validation checks passed ✅")

    else:
        print("\nValidation failed ❌")


    return passed