# The Digital Translator

A five-tier Python learning project that explores how real-world goals become precise instructions, algorithms, data representations, and working programs.

The project progresses from a step-by-step breakfast assistant to an online-store simulation, connecting the core ideas behind how computer systems work.

## Project Objective

Develop the digital translator mindset:

> Take something a person wants to accomplish and translate it into explicit instructions and meaningful data that a computer can process.

Each tier explores a different part of this process.

| Tier | Project | Main concept |
|---|---|---|
| 1 | Literal Assistant | Precise instructions and hidden assumptions |
| 2 | ATM Simulator | Algorithms, decisions, and failure handling |
| 3 | Simple Calculator | Input → Processing → Output |
| 4 | Customer Data Translator | Data types and digital representation |
| 5 | Online Store Simulator | Connecting input, instructions, processing, storage, and output |

## Requirements

- Python 3
- A terminal or command prompt
- A text editor or IDE

All programs use Python’s standard library. No third-party packages are required.

## Project Structure

The project uses the following files:

```text
project-folder/
├── main.py          # Tier 1: Literal Assistant
├── tier2.py         # Tier 2: ATM Simulator
├── tier3.py         # Tier 3: Simple Calculator
├── tier4.py         # Tier 4: Customer Data Translator
├── tier5.py         # Tier 5: Online Store Simulator
├── README.md
└── demo_orders/     # Created when the store saves an order
```

The `demo_orders` directory is created automatically when a demo order is successfully saved.

## Running the Projects

Open a terminal in the project directory and run the relevant command:

| Tier | Command |
|---|---|
| 1 | `python3 main.py` |
| 2 | `python3 tier2.py` |
| 3 | `python3 tier3.py` |
| 4 | `python3 tier4.py` |
| 5 | `python3 tier5.py` |

Use fictional customer information, card details, and addresses when testing. These programs are educational simulations, not production banking or shopping systems.

---

## Tier 1: The Literal Assistant

### The Challenge

Translate this broad instruction into an ordered procedure:

```text
Make me breakfast.
```

A person may fill in missing details using experience and context. The program needs those details to be supplied explicitly.

### Implementation

The assistant recognizes the request:

```text
make me breakfast
```

It then displays 21 instructions for preparing eggs, toast, and tea and serving them at the dining table.

The user presses Enter after each instruction. The completion message appears only after the final step is confirmed.

### Run

```bash
python3 main.py
```

### Example

```text
Welcome to the Literal Assistant!
I can help you prepare breakfast.
What would you like me to do? make me breakfast
Your task is: make me breakfast

Starting breakfast preparation...

Step 1: Go to the kitchen.
Press Enter when you have completed this step...
```

After the final confirmation:

```text
Breakfast preparation instructions completed!
```

### Concepts Practiced

- Receiving text with `input()`.
- Displaying information with `print()`.
- Storing instructions in a list.
- Matching a supported request using `if` and `else`.
- Normalizing input with `.strip()` and `.lower()`.
- Iterating with `for`.
- Numbering instructions with `enumerate()`.
- Using indentation to control execution.

### Assumptions Identified

The original request did not specify:

- Which breakfast to prepare.
- How many people to serve.
- Ingredient quantities.
- Ingredient and equipment locations.
- How the eggs should be prepared.
- How to prepare the tea.
- Where the finished meal should be placed.
- How to determine whether each action is complete.

The implementation makes some decisions explicit, but instructions such as “prepare one cup of tea” still contain missing detail.

### Important Limitation

The program displays instructions; it does not prepare food or verify physical actions.

Pressing Enter means the user has supplied input. It does not prove that a step was completed. Any entered text followed by Enter also advances the current version.

### Learning Outcome

Breaking a broad request into steps reveals hidden assumptions. A precise procedure also needs defined starting conditions, completion checks, and responses to problems.

---

## Tier 2: ATM Simulator

### The Challenge

Turn this goal into an algorithm:

```text
Withdraw money from an ATM.
```

The algorithm must describe both the successful path and what happens when a step fails.

### Implementation

The simulator:

1. Requests a demo card number.
2. Verifies the supported card.
3. Requests and validates the PIN.
4. Allows up to three incorrect PIN attempts.
5. Displays a transaction menu.
6. Validates a requested withdrawal amount.
7. Checks the transaction limit, account balance, and ATM cash.
8. Requests confirmation.
9. Simulates transaction success or failure.
10. Updates in-memory balances only after simulated success.

### Run

```bash
python3 tier2.py
```

### Demo Settings

| Setting | Value |
|---|---|
| Card number | `1234567890123456` |
| PIN | `1234` |
| Starting account balance | NGN 150,000 |
| Starting ATM cash | NGN 100,000 |
| Per-transaction withdrawal limit | NGN 50,000 |
| Available banknote | NGN 1,000 |
| Transaction fee | NGN 0 |

The PIN is normally hidden while typing.

### Menu

```text
ATM Menu
1. Withdraw money
2. Check balance
3. Exit
Choose an option:
```

### Successful Withdrawal Example

Enter:

```text
Menu option: 1
Amount: 5000
Confirmation: yes
Demo transaction result: success
```

Expected result:

```text
Withdrawal successful.
Please collect your cash: NGN 5,000.00
Remaining account balance: NGN 145,000.00
```

### Failure Handling

| Situation | Program response |
|---|---|
| Malformed card input | Requests a readable 16-digit card number. |
| Unsupported card | Rejects the card and closes the session. |
| Incorrect PIN | Allows retries within the three-attempt limit. |
| Invalid withdrawal input | Requests a valid positive whole-number amount. |
| Amount not divisible by 1,000 | Explains the available banknote restriction. |
| Transaction limit exceeded | Rejects the amount. |
| Insufficient account balance | Requests a smaller amount or cancellation. |
| Insufficient ATM cash | Requests a smaller amount or cancellation. |
| Simulated transaction failure | Leaves both balances unchanged. |

### Concepts Practiced

- Breaking an algorithm into functions.
- Conditional decisions.
- Loops and retry limits.
- Input validation.
- Returning values from functions.
- Maintaining state during a session.
- Handling interrupted or ended input.

### Important Limitations

- Card verification is a comparison with a fictional number.
- The PIN is hard-coded for demonstration.
- No bank connection or physical cash dispenser exists.
- Balances reset when the program restarts.
- The success/failure prompt is a testing control.
- Partial cash dispensing and uncertain transaction outcomes are not implemented.
- The closing message does not physically return a card.

### Learning Outcome

```text
Problem → Algorithm → Program
```

The problem states the goal. The algorithm describes the solution procedure. The program implements that procedure as executable instructions.

---

## Tier 3: Simple Calculator

### The Challenge

Design and implement a calculator using:

```text
Input → Processing → Output
```

### Implementation

The calculator:

1. Receives two numbers.
2. Receives a supported operation.
3. Validates the inputs.
4. Checks for division by zero.
5. Performs the calculation.
6. Displays the result.
7. Offers another calculation.

### Run

```bash
python3 tier3.py
```

### Supported Operations

| Operation | Input | Processing | Expected output |
|---|---|---|---|
| Addition | `20`, `5`, `+` | `20 + 5` | `25.0` |
| Subtraction | `20`, `5`, `-` | `20 - 5` | `15.0` |
| Multiplication | `20`, `5`, `*` | `20 × 5` | `100.0` |
| Division | `20`, `5`, `/` | `20 ÷ 5` | `4.0` |

### Example

```text
Welcome to the Simple Calculator!

Enter the first number: 20
Enter the second number: 5
Choose an operation (+, -, *, /): +

Result: 20.0 + 5.0 = 25.0

Would you like another calculation? (yes/no):
```

### Error Handling

- Blank or nonnumeric entries trigger another prompt.
- Unsupported operations are rejected.
- Division by zero requests a nonzero second number.
- Infinity and `NaN` are rejected.
- A nonfinite result produces a range message instead of an ordinary result.
- Interrupted or ended input closes the calculator with a message.

### Division-by-Zero Reasoning

For:

```text
20 ÷ 0
```

the program should not invent an answer or continue as if the calculation succeeded.

It displays:

```text
Cannot divide by zero.
```

and asks for a replacement second number.

Zero remains valid in other calculations, including:

```text
20 + 0 = 20
20 × 0 = 0
0 ÷ 5 = 0
```

### Concepts Practiced

- Numeric conversion with `float()`.
- Catching `ValueError`.
- Arithmetic operations.
- Conditional branching.
- Finite-number validation.
- Reusable input functions.

### Learning Outcome

Processing includes validation and decision-making—not just arithmetic. A useful output may be a result or an explanation of why the requested operation cannot proceed.

---

## Tier 4: Customer Data Translator

### The Challenge

Represent the following information using suitable data types:

```text
Customer name: Victor
Age: 30
Account balance: 150000.50
Account active: Yes
```

### Chosen Representations

| Information | Meaning | Python representation |
|---|---|---|
| `"Victor"` | Customer name | `str` |
| `30` | Age in whole years | `int` |
| `Decimal("150000.50")` | Account balance | `Decimal` |
| `True` | Account is active | `bool` |

The example does not specify a currency, so the program does not assign one.

### Run

```bash
python3 tier4.py
```

### Implementation

The program:

1. Creates the customer values.
2. Displays them in a readable format.
3. Shows the Python type of each value.
4. Uses the Boolean account status in a decision.
5. Encodes the name into UTF-8 bytes.
6. Displays a binary view of those bytes.

### Example Output

```text
Customer Data Translator
------------------------
Customer name: Victor
Age: 30
Account balance: 150,000.50
Account active: Yes

Python Data Types
-----------------
Customer name: str
Age: int
Account balance: Decimal
Account active: bool
```

### Representation Versus Display

The program uses:

```python
account_active = True
```

for its decision-making, but displays:

```text
Account active: Yes
```

Likewise, the balance is a numerical value, while commas and decimal places are part of its presentation.

### Digital Representation

The text demonstration follows this chain:

```text
Customer name
      ↓
UTF-8 encoding
      ↓
Bytes
      ↓
Binary view of the bytes
```

This demonstrates one encoding process. It is not a complete display of Python’s internal object memory, and it does not mean every data type uses the same representation.

### Why Correct Representation Matters

If the balance is entered incorrectly or interpreted using the wrong scale, the system could:

- Display the wrong balance.
- Approve a transaction that should be rejected.
- Reject a transaction that should be allowed.
- Produce inaccurate records.

Using a suitable type does not automatically correct inaccurate source data.

### Learning Outcome

Data is information represented in a form a computer can store, process, and communicate. Correct processing depends on preserving both the value and its meaning.

---

## Tier 5: Online Store Simulator

### The Challenge

Explain and demonstrate a complete system:

```text
Customer input
      ↓
Application and instructions
      ↓
Data processing
      ↓
Stored data
      ↓
Result / output
```

### Implementation

The demo store sells headphones and:

1. Displays the product and price.
2. Requests a fictional customer name.
3. Validates the requested quantity.
4. Requests a fictional delivery address.
5. Calculates the total.
6. Displays an order summary.
7. Requests confirmation.
8. Simulates payment success or failure.
9. Saves a confirmed order as JSON.
10. Displays the result.

### Run

```bash
python3 tier5.py
```

### Demo Settings

| Setting | Value |
|---|---|
| Product | Headphones |
| Product ID | `HP001` |
| Unit price | NGN 50,000 |
| Allowed quantity | 1–10 per order |
| Delivery charge | NGN 0 |
| Payment | Simulated |
| Storage | One JSON file per confirmed order |

### Example

```text
Enter a demo customer name: Victor
Enter quantity: 2
Enter a fictional delivery address: 10 Example Street
```

The order summary includes:

```text
Product: Headphones
Quantity: 2
Delivery charge: NGN 0.00
Total: NGN 100,000.00
```

To complete the simulation:

```text
Confirm this order? (yes/no): yes
Simulate payment — enter 'success' or 'fail': success
```

If saving succeeds, the program displays an order confirmation and order ID.

### Stored Information

Each confirmed order records:

- Order ID.
- Customer name.
- Fictional delivery address.
- Product ID and name.
- Unit price.
- Quantity.
- Total.
- Currency.
- Simulated payment status.
- Order status.

Records are written to the automatically created `demo_orders` directory.

### Failure Handling

| Situation | Program response |
|---|---|
| Blank name or address | Requests a nonempty value. |
| Nonnumeric quantity | Requests a whole number. |
| Quantity outside 1–10 | Explains the allowed range. |
| Customer declines confirmation | Cancels without attempting payment simulation. |
| Simulated payment fails | Does not save a confirmed order. |
| Saving fails | Reports a storage error instead of announcing confirmation. |

### Important Limitations

- No real payment is processed.
- No delivery is arranged.
- The quantity limit is not persistent inventory tracking.
- Authentication, taxes, refunds, and real payment reconciliation are not implemented.
- Saved customer details are readable demo data.
- A confirmed order record does not prove that goods were shipped or delivered.

Use fictional information only. Review generated records before sharing the repository.

### Learning Outcome

The store connects the earlier tiers: explicit instructions define behavior, an algorithm orders the actions, data types represent information, processing produces new values, storage preserves records, and output communicates the result.

---

## Suggested Manual Tests

| Tier | Test | Expected outcome |
|---|---|---|
| 1 | Enter `make me breakfast` | Displays the breakfast instructions sequentially. |
| 1 | Enter an unsupported request | Displays the unrecognized-task message. |
| 2 | Enter the wrong PIN three times | Ends the session. |
| 2 | Withdraw 5,000 with simulated success | Deducts 5,000 from the in-memory account and ATM balances. |
| 2 | Choose simulated failure | Leaves balances unchanged. |
| 3 | Calculate `20 / 5` | Displays `4.0`. |
| 3 | Attempt `20 / 0` | Requests a nonzero second number. |
| 4 | Run the program | Displays customer values, types, and encoded-name information. |
| 5 | Confirm an order for two units with simulated payment success | Saves an order totaling NGN 100,000. |
| 5 | Choose simulated payment failure | Does not save a confirmed order. |

## Troubleshooting

### The program cannot be found

Check that the terminal is open in the project directory and that the filename matches the command.

### The PIN does not appear while typing

The ATM simulator normally hides PIN input. Type `1234` and press Enter.

### Changes do not appear when running

Save the file and confirm that you are running the correct tier.

### An indentation or syntax error appears

Check the indicated line and the surrounding code. Preserve indentation when copying Python blocks, especially around `if`, `else`, loops, and `try` / `except`.

### An order file is missing

A confirmed order is saved only after confirmation, simulated payment success, and successful file writing. Check the `demo_orders` folder beside `tier5.py`.

---

## Final Reflection

> “A computer does not understand the real world directly. It works with representations of information and follows instructions for processing those representations.”

In my own words, a real-world goal must be translated into data and explicit instructions before a program can act on it.

The breakfast assistant showed me how much information can be hidden in a simple request. The ATM exercise showed why a procedure needs decisions, retries, and failure paths. The calculator demonstrated input, processing, and output. The customer-data exercise showed why different information needs different representations. The online store connected those ideas into one system.

I also learned that a program can follow its instructions correctly and still produce an unsuitable result if the instructions are incomplete, the input is wrong, or the data is interpreted incorrectly.

Writing a program is therefore not only about syntax. It is about defining the problem, identifying assumptions, choosing meaningful data, designing a procedure, and deciding how success and failure should be communicated.

## Capstone Mental Model

```text
REAL-WORLD PROBLEM
        ↓
DATA
        ↓
PROGRAM AND INSTRUCTIONS
        ↓
PROCESSING
        ↓
STORED DATA, WHEN NEEDED
        ↓
OUTPUT
```

The digital translator mindset means asking:

- What does the user want to accomplish?
- What information is required?
- Which assumptions must become explicit?
- What steps and decisions are necessary?
- What could go wrong?
- What should the system remember?
- What should the user receive?
- How will the system determine whether it succeeded?