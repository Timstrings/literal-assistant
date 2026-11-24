print("Welcome to the Literal Assistant!")
print("I can help you prepare breakfast.")

task = input("What would you like me to do? ")

print("Your task is:", task)

if task.strip().lower() == "make me breakfast":
    print("\nStarting breakfast preparation...")

    breakfast_steps = [
        "Go to the kitchen.",
        "Locate the refrigerator.",
        "Open the refrigerator.",
        "Collect two fresh eggs.",
        "Get a frying pan, cooking oil and cooking spoon.",
        "Place the frying pan on the stove.",
        "Add one tablespoon of cooking oil.",
        "Turn on the stove to medium heat.",
        "Break two eggs into a clean bowl.",
        "Pour the eggs into the frying pan.",
        "Cook until the eggs are fully cooked.",
        "Turn off the stove.",
        "Place two slices of bread in the toaster.",
        "Toast the bread until golden brown.",
        "Prepare one cup of tea.",
        "Place the eggs and bread on a plate.",
        "Place the tea beside the plate.",
        "Carry the plate and cup of tea carefully to the dining table.",
        "Set the plate and cup of tea on the dining table.",
        "Place cutlery and a napkin beside the plate.",
        "Confirm that breakfast is ready.",
    ]

    for step_number, instruction in enumerate(breakfast_steps, start=1):
        print(f"\nStep {step_number}: {instruction}")
        input("Press Enter when you have completed this step...")

    print("\nBreakfast preparation instructions completed!")

else:
    print("Sorry, I don't understand that task.")