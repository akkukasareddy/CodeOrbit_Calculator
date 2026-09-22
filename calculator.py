"""
Simple Calculator (Enhanced)
CodeOrbit Tech - Python Programming Internship

An upgraded version of the basic calculator with:
  - More operations (power, square root, modulus)
  - A "memory" you can reuse in the next calculation
  - A history of past calculations you can review
  - Cleaner output formatting (no ugly trailing decimals)
  - Operations organized in a dictionary instead of a long if/elif chain
"""

import math

OPERATIONS = {
    "1": ("Add (+)", lambda a, b: a + b, "+"),
    "2": ("Subtract (-)", lambda a, b: a - b, "-"),
    "3": ("Multiply (*)", lambda a, b: a * b, "*"),
    "4": ("Divide (/)", lambda a, b: a / b, "/"),          # may raise ZeroDivisionError
    "5": ("Power (^)", lambda a, b: a ** b, "^"),
    "6": ("Modulus (%)", lambda a, b: a % b, "%"),          # may raise ZeroDivisionError
}

SQRT_CHOICE = "7"
HISTORY_CHOICE = "8"
EXIT_CHOICE = "9"


class Calculator:
    """Keeps track of calculation history and the last result (memory)."""

    def __init__(self):
        self.history = []
        self.memory = None

    def record(self, expression, result):
        """Save a calculation to history and update memory with the result."""
        self.history.append(f"{expression} = {format_number(result)}")
        self.memory = result

    def show_history(self):
        print("\n--- Calculation History ---")
        if not self.history:
            print("No calculations yet.")
        else:
            for i, entry in enumerate(self.history, start=1):
                print(f"{i}. {entry}")
        print()


def format_number(value):
    """
    Format a number for display: show whole numbers without a decimal
    point, and round others to a sensible number of decimal places
    instead of printing long float artifacts like 0.3333333333333333.
    """
    rounded = round(value, 6)
    if rounded == int(rounded):
        return str(int(rounded))
    return str(rounded)


def get_number(prompt, calculator):
    """
    Prompt the user for a number. Typing 'M' reuses the last result
    stored in memory (if any). Re-asks until valid input is given.
    """
    while True:
        raw = input(prompt).strip()
        if raw.upper() == "M":
            if calculator.memory is not None:
                print(f"(using memory: {format_number(calculator.memory)})")
                return calculator.memory
            print("Memory is empty. Enter a number instead.\n")
            continue
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number, or 'M' for memory.\n")


def show_menu():
    print("\n=== Calculator Menu ===")
    for key, (label, _, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    print(f"{SQRT_CHOICE}. Square Root")
    print(f"{HISTORY_CHOICE}. View History")
    print(f"{EXIT_CHOICE}. Exit")


def get_choice():
    valid_choices = set(OPERATIONS) | {SQRT_CHOICE, HISTORY_CHOICE, EXIT_CHOICE}
    while True:
        choice = input(f"Enter choice (1-{EXIT_CHOICE}): ").strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter a number from 1 to {EXIT_CHOICE}.")


def main():
    print("=== Simple Calculator (Enhanced) ===")
    print("Tip: type 'M' at a number prompt to reuse your last result.")
    calculator = Calculator()

    while True:
        show_menu()
        choice = get_choice()

        if choice == EXIT_CHOICE:
            print("Goodbye!")
            break

        if choice == HISTORY_CHOICE:
            calculator.show_history()
            continue

        try:
            if choice == SQRT_CHOICE:
                num = get_number("Enter number: ", calculator)
                if num < 0:
                    raise ValueError("Cannot take the square root of a negative number.")
                result = math.sqrt(num)
                expression = f"sqrt({format_number(num)})"
            else:
                label, func, symbol = OPERATIONS[choice]
                num1 = get_number("Enter first number (or 'M'): ", calculator)
                num2 = get_number("Enter second number (or 'M'): ", calculator)
                result = func(num1, num2)  # may raise ZeroDivisionError
                expression = f"{format_number(num1)} {symbol} {format_number(num2)}"

            print(f"\nResult: {expression} = {format_number(result)}\n")
            calculator.record(expression, result)

        except ZeroDivisionError:
            print("\nError: Cannot divide (or take modulus) by zero. Please try again.\n")
        except ValueError as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()




    
