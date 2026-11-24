"""Tier 3: A simple input-processing-output calculator."""

from math import isfinite


def get_number(prompt):
    """Ask again until the user enters a valid, finite number."""
    while True:
        entry = input(prompt).strip()

        try:
            number = float(entry)
        except ValueError:
            print("Invalid input. Enter a number, such as 20 or 5.5.")
            continue

        if not isfinite(number):
            print("Enter a finite number, not infinity or NaN.")
            continue

        return number


def get_operation():
    """Ask the user to select a supported operation."""
    while True:
        operation = input(
            "Choose an operation (+, -, *, /): "
        ).strip()

        if operation in {"+", "-", "*", "/"}:
            return operation

        print("Invalid operation. Choose +, -, *, or /.")


def run_calculator():
    """Receive input, process it, and display the result."""
    print("Welcome to the Simple Calculator!")

    while True:
        # INPUT
        number_1 = get_number("\nEnter the first number: ")
        number_2 = get_number("Enter the second number: ")
        operation = get_operation()

        # Validate division before calculating.
        while operation == "/" and number_2 == 0:
            print("Cannot divide by zero.")
            number_2 = get_number("Enter a nonzero second number: ")

        # PROCESSING
        if operation == "+":
            result = number_1 + number_2
        elif operation == "-":
            result = number_1 - number_2
        elif operation == "*":
            result = number_1 * number_2
        else:
            result = number_1 / number_2

        # OUTPUT
        if isfinite(result):
            print(f"\nResult: {number_1} {operation} {number_2} = {result}")
        else:
            print("\nThe result is outside this calculator's finite range.")

        while True:
            again = input(
                "\nWould you like another calculation? (yes/no): "
            ).strip().lower()

            if again in {"yes", "no"}:
                break

            print("Please enter 'yes' or 'no'.")

        if again == "no":
            print("Thank you for using the Simple Calculator!")
            return


def main():
    try:
        run_calculator()
    except KeyboardInterrupt:
        print("\nCalculator stopped by the user.")
    except EOFError:
        print("\nInput ended. Calculator closed.")


if __name__ == "__main__":
    main()