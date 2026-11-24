"""Tier 5: An educational online-store simulation."""

import json
from pathlib import Path
from uuid import uuid4


PRODUCT = {
    "id": "HP001",
    "name": "Headphones",
    "price_naira": 50_000,
}

MAX_QUANTITY = 10

# Store demo order files beside this Python file.
ORDERS_DIRECTORY = Path(__file__).resolve().parent / "demo_orders"


def get_required_text(prompt):
    """Reject empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_quantity():
    """Request a whole-number quantity within the demo limit."""
    while True:
        entry = input("Enter quantity: ").strip()

        try:
            quantity = int(entry)
        except ValueError:
            print("Enter a whole number, such as 1 or 2.")
            continue

        if 1 <= quantity <= MAX_QUANTITY:
            return quantity

        print(f"Quantity must be between 1 and {MAX_QUANTITY}.")


def get_choice(prompt, choices):
    """Request one of the permitted responses."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in choices:
            return choice

        print(f"Choose one of: {', '.join(sorted(choices))}.")


def save_order(order):
    """Save one confirmed demo order in its own JSON file."""
    ORDERS_DIRECTORY.mkdir(exist_ok=True)

    order_file = ORDERS_DIRECTORY / f"{order['order_id']}.json"

    with order_file.open("x", encoding="utf-8") as file:
        json.dump(order, file, indent=4, ensure_ascii=False)

    return order_file


def run_store():
    print("Welcome to the Demo Online Store!")
    print("Use fictional details. No real payment will be taken.")

    print(f"\nProduct: {PRODUCT['name']}")
    print(f"Unit price: NGN {PRODUCT['price_naira']:,.2f}")
    print(f"Maximum quantity per order: {MAX_QUANTITY}")

    # 1. CUSTOMER INPUT
    customer_name = get_required_text("\nEnter a demo customer name: ")
    quantity = get_quantity()
    address = get_required_text("Enter a fictional delivery address: ")

    # 2. PROCESSING
    total = PRODUCT["price_naira"] * quantity

    print("\nOrder Summary")
    print("-------------")
    print(f"Customer: {customer_name}")
    print(f"Product: {PRODUCT['name']}")
    print(f"Quantity: {quantity}")
    print(f"Delivery address: {address}")
    print("Delivery charge: NGN 0.00")
    print(f"Total: NGN {total:,.2f}")

    confirmation = get_choice(
        "\nConfirm this order? (yes/no): ",
        {"yes", "no"},
    )

    if confirmation == "no":
        print("Order cancelled. No payment was attempted.")
        return

    # 3. SIMULATED PAYMENT
    payment_result = get_choice(
        "Simulate payment — enter 'success' or 'fail': ",
        {"success", "fail"},
    )

    if payment_result == "fail":
        print("\nPayment simulation failed.")
        print("Order not confirmed. No confirmed order was saved.")
        return

    # 4. PREPARE STORED DATA
    order = {
        "order_id": uuid4().hex,
        "customer_name": customer_name,
        "delivery_address": address,
        "product_id": PRODUCT["id"],
        "product_name": PRODUCT["name"],
        "unit_price_naira": PRODUCT["price_naira"],
        "quantity": quantity,
        "total_naira": total,
        "currency": "NGN",
        "payment_status": "simulated_success",
        "order_status": "confirmed",
    }

    # Do not announce confirmation unless saving succeeds.
    try:
        order_file = save_order(order)
    except OSError as error:
        print("\nThe order could not be saved.")
        print("Order not confirmed. No real payment was taken.")
        print(f"Storage error: {error}")
        return

    # 5. OUTPUT
    print("\nOrder confirmed!")
    print(f"Order ID: {order['order_id']}")
    print(f"Total: NGN {total:,.2f}")
    print("Payment: simulated success — no real money taken.")
    print(f"Demo order record: {order_file.name}")
    print("Thank you for using the Demo Online Store!")


def main():
    try:
        run_store()
    except KeyboardInterrupt:
        print("\nStore session interrupted. No real payment was taken.")
    except EOFError:
        print("\nInput ended. Store session closed.")


if __name__ == "__main__":
    main()