# literal-assistant

# Literal Assistant

A beginner-friendly Python command-line project that turns a broad request—“make me breakfast”—into a sequence of explicit instructions.

## Project Objective

Demonstrate why computers require precise, explicit instructions.

Humans routinely fill in missing information using experience and context. A program, however, cannot reliably fill those gaps unless its instructions and available information support that behavior.

This project explores that difference by breaking a familiar everyday task into individual steps.

## How It Works

The Literal Assistant:

1. Welcomes the user.
2. Asks what task they want help with.
3. Checks whether the request is `make me breakfast`.
4. Displays breakfast preparation and serving instructions one at a time.
5. Waits for the user to press Enter after each instruction.
6. Displays a completion message after the final confirmation.

If the request is not recognized, the assistant displays:

```text
Sorry, I don't understand that task.
```

## Features

- Command-line interaction.
- Recognition of the supported breakfast request.
- Case-insensitive request matching.
- Removal of leading and trailing spaces from the request.
- A numbered sequence of 21 instructions.
- Step-by-step confirmation using Enter.
- Instructions for serving breakfast at the dining table.
- A completion message that appears only after all steps are confirmed.

## Requirements

- Python 3
- A terminal or command prompt

No third-party packages are required.

## Getting Started

Save the program as `main.py`, then open a terminal in the project directory and run:

```bash
python3 main.py
```

When prompted, enter:

```text
make me breakfast
```

Press Enter after completing each instruction to move to the next step.

## Example Interaction

```text
Welcome to the Literal Assistant!
I can help you prepare breakfast.
What would you like me to do? make me breakfast
Your task is: make me breakfast

Starting breakfast preparation...

Step 1: Go to the kitchen.
Press Enter when you have completed this step...

Step 2: Locate the refrigerator.
Press Enter when you have completed this step...
```

The interaction continues through the preparation and serving steps. At the end:

```text
Step 21: Confirm that breakfast is ready.
Press Enter when you have completed this step...

Breakfast preparation instructions completed!
```

## Demonstration: From a Broad Request to Explicit Steps

The request:

```text
Make me breakfast.
```

sounds straightforward to a person, but it leaves many decisions unstated:

- What food should be prepared?
- How much food is needed?
- Which ingredients and equipment should be used?
- In what order should the actions happen?
- How should the meal be served?
- What counts as completing the task?

The assistant addresses some of these gaps by providing an ordered list of actions, from going to the kitchen to serving breakfast at the dining table.

However, breaking a task into steps does not automatically make every step precise. An instruction can still contain hidden assumptions.

## Reflection: Assumptions in My Instructions

While turning the original request into a program, I made the following assumptions:

| Area | Assumption |
|---|---|
| Meal choice | Breakfast means eggs, toast, and tea. |
| Quantity | Two eggs, two slices of bread, and one cup of tea are appropriate. |
| Supplies | The required ingredients and equipment are available. |
| Location | The user knows where the kitchen, refrigerator, and dining table are. |
| Cooking method | The eggs should be fried rather than prepared another way. |
| Tea preferences | The user knows how to prepare tea and can decide whether to add milk or sugar. |
| Cooking completion | The user can recognize fully cooked eggs and golden-brown toast. |
| Serving | The meal should be served at the dining table with cutlery and a napkin. |

These assumptions show how much information can be hidden inside an apparently simple instruction.

## Instructions That Still Need More Detail

Some steps remain too broad for a fully specified process:

- “Collect two fresh eggs” does not explain how to determine freshness.
- “Break two eggs into a clean bowl” does not explain what to do if shell pieces fall into the bowl.
- “Cook until the eggs are fully cooked” does not define a precise completion check.
- “Prepare one cup of tea” combines several unspecified actions.
- The instructions collect a cooking spoon but do not explain when to use it.
- The program does not define an alternative if an ingredient or appliance is unavailable.

These gaps are part of the project's lesson: precise instructions require attention to details, dependencies, and possible problems.

## What the Program Actually Does

The assistant displays instructions. It does not physically prepare breakfast.

Pressing Enter tells the program to continue, but it does not prove that the displayed action was completed. The assistant cannot inspect the kitchen, check ingredients, or verify the finished meal.

The final message therefore confirms that the instruction sequence has been completed in the program—not that breakfast has been independently verified.

## Python Concepts Practiced

| Concept | Use in this project |
|---|---|
| `print()` | Display greetings, instructions, and messages. |
| `input()` | Receive the user's request and pause between steps. |
| Variables | Store the requested task. |
| Lists | Store the ordered breakfast instructions. |
| `.strip()` and `.lower()` | Normalize the user's task request. |
| `if` / `else` | Choose between the supported task and an unrecognized request. |
| `for` loops | Process the instructions one at a time. |
| `enumerate()` | Number the steps automatically. |
| f-strings | Combine step numbers and instructions in the output. |
| Indentation | Control which statements run inside each block. |

## Current Limitations

- Only one task is supported.
- The request must match `make me breakfast` after whitespace and case normalization.
- Any response followed by Enter advances the current step.
- The program does not verify physical task completion.
- Meal preferences, serving quantities, and dietary requirements are not collected.
- Missing ingredients and equipment are not handled.
- Keyboard interruptions and end-of-input exceptions are not explicitly handled in the current version.

## Possible Improvements

- Require an explicit `done` response before advancing.
- Add commands to repeat a step or stop the session.
- Ask about meal preferences and the number of people being served.
- Check ingredient and equipment availability.
- Break broad instructions into smaller, clearer actions.
- Handle interrupted or unavailable input gracefully.
- Support additional tasks.

## Key Takeaway

Writing instructions is not just about listing actions. It also means identifying assumptions, defining completion conditions, and deciding what should happen when something unexpected occurs.

The Literal Assistant demonstrates that a program is only as explicit as the instructions and information provided to it.