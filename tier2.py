"""Educational ATM withdrawal simulator. No real banking connection."""

from getpass import getpass


# Demo settings — never use real card details or PINs here.
DEMO_CARD = "1234567890123456"
DEMO_PIN = "1234"

STARTING_BALANCE = 150_000
STARTING_ATM_CASH = 100_000

MAX_PIN_ATTEMPTS = 3
WITHDRAWAL_LIMIT = 50_000
BANKNOTE_VALUE = 1_000


def read_choice(prompt, allowed_choices):
    """Keep asking until the user enters an allowed choice."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in allowed_choices:
            return choice

        print("Invalid choice. Please try again.")


def verify_card():
    """Simulate inserting and reading a card."""
    while True:
        card = input(
            "\nEnter the demo card number, or 'cancel': "
        ).strip()

        if card.lower() == "cancel":
            return False

        if len(card) != 16 or not card.isascii() or not card.isdigit():
            print("Card could not be read. Enter exactly 16 digits.")
            continue

        if card != DEMO_CARD:
            print("This card is not supported by the demo ATM.")
            return False

        print("Card verified.")
        return True


def verify_pin():
    """Allow a limited number of PIN attempts."""
    for attempt in range(1, MAX_PIN_ATTEMPTS + 1):
        pin = getpass("Enter your PIN, or type 'cancel': ")

        if pin.lower() == "cancel":
            return False

        if pin == DEMO_PIN:
            print("PIN verified.")
            return True

        remaining = MAX_PIN_ATTEMPTS - attempt

        if remaining > 0:
            print(f"Incorrect PIN. Attempts remaining: {remaining}")
        else:
            print("PIN attempt limit reached. Session ended.")

    return False


def request_amount(balance, atm_cash):
    """Return a valid withdrawal amount, or None for cancellation."""
    while True:
        entry = input(
            "\nEnter an amount in whole naira, or 'cancel': "
        ).strip()

        if entry.lower() == "cancel":
            return None

        if not entry:
            print("Please enter an amount.")
            continue

        # Limit input length and accept only ordinary decimal digits.
        if (
            len(entry) > 12
            or not entry.isascii()
            or not entry.isdigit()
        ):
            print("Enter a positive whole number, such as 5000.")
            continue

        amount = int(entry)

        if amount == 0:
            print("The withdrawal amount must be greater than zero.")
        elif amount > WITHDRAWAL_LIMIT:
            print(
                "The per-transaction withdrawal limit is "
                f"NGN {WITHDRAWAL_LIMIT:,.2f}."
            )
        elif amount % BANKNOTE_VALUE != 0:
            print(
                "This demo ATM dispenses only NGN 1,000 notes. "
                "Enter a multiple of 1000."
            )
        elif amount > balance:
            print("Insufficient account balance. Try a smaller amount.")
        elif amount > atm_cash:
            print("The ATM has insufficient cash. Try a smaller amount.")
        else:
            return amount


def process_withdrawal(amount, balance, atm_cash):
    """Simulate a transaction with a definite success or failure."""
    print("\nTransaction summary")
    print("-------------------")
    print(f"Withdrawal: NGN {amount:,.2f}")
    print("Fee:        NGN 0.00")
    print(f"Total:      NGN {amount:,.2f}")

    confirmation = read_choice(
        "Confirm withdrawal? (yes/no): ",
        {"yes", "no"},
    )

    if confirmation == "no":
        print("Withdrawal cancelled. No money was deducted.")
        return balance, atm_cash

    # This option makes the failure branch easy to test.
    result = read_choice(
        "Demo transaction result — enter 'success' or 'fail': ",
        {"success", "fail"},
    )

    if result == "fail":
        print("Transaction could not be completed.")
        print("No cash was dispensed and no money was deducted.")
        return balance, atm_cash

    # In this simulation, 'success' represents confirmed cash dispensing.
    balance -= amount
    atm_cash -= amount

    print("\nWithdrawal successful.")
    print(f"Please collect your cash: NGN {amount:,.2f}")
    print(f"Remaining account balance: NGN {balance:,.2f}")

    return balance, atm_cash


def run_session():
    """Run one authenticated ATM session."""
    balance = STARTING_BALANCE
    atm_cash = STARTING_ATM_CASH

    print("Welcome to the Demo ATM")
    print("This simulator does not use real money.")

    if not verify_card():
        return

    if not verify_pin():
        return

    while True:
        print("\nATM Menu")
        print("1. Withdraw money")
        print("2. Check balance")
        print("3. Exit")

        choice = read_choice("Choose an option: ", {"1", "2", "3"})

        if choice == "1":
            if balance < BANKNOTE_VALUE:
                print("Your balance is too low for a withdrawal.")
                continue

            if atm_cash < BANKNOTE_VALUE:
                print("The ATM has no cash available for withdrawal.")
                continue

            amount = request_amount(balance, atm_cash)

            if amount is None:
                print("Withdrawal cancelled.")
                continue

            balance, atm_cash = process_withdrawal(
                amount,
                balance,
                atm_cash,
            )

        elif choice == "2":
            print(f"Available balance: NGN {balance:,.2f}")

        else:
            return


def main():
    """Handle interrupted input and always close the demo session."""
    try:
        run_session()
    except KeyboardInterrupt:
        print("\nSession interrupted by the user.")
    except EOFError:
        print("\nInput ended. Closing the session.")
    finally:
        print("\nSession closed. Please collect your card if inserted.")
        print("Thank you for using the Demo ATM.")


if __name__ == "__main__":
    main()