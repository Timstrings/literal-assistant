"""Tier 4: Represent customer information using appropriate data types."""

from decimal import Decimal


def main():
    # Represent the original customer information.
    customer_name = "Victor"
    age = 30
    account_balance = Decimal("150000.50")
    account_active = True

    print("Customer Data Translator")
    print("------------------------")

    # Display information in a human-friendly form.
    print(f"Customer name: {customer_name}")
    print(f"Age: {age}")
    print(f"Account balance: {account_balance:,.2f}")

    status = "Yes" if account_active else "No"
    print(f"Account active: {status}")

    # Display the type used for each value.
    print("\nPython Data Types")
    print("-----------------")
    print(f"Customer name: {type(customer_name).__name__}")
    print(f"Age: {type(age).__name__}")
    print(f"Account balance: {type(account_balance).__name__}")
    print(f"Account active: {type(account_active).__name__}")

    # Demonstrate a decision based on a Boolean.
    print("\nAccount Status Check")
    print("--------------------")

    if account_active:
        print("The account is active.")
    else:
        print("The account is inactive.")

    # Demonstrate encoding text as bytes.
    print("\nText Encoding Demonstration")
    print("---------------------------")

    name_bytes = customer_name.encode("utf-8")
    name_binary = " ".join(
        format(byte, "08b") for byte in name_bytes
    )

    print(f"Original text: {customer_name}")
    print(f"UTF-8 bytes: {list(name_bytes)}")
    print(f"Binary view of those bytes: {name_binary}")


if __name__ == "__main__":
    main()