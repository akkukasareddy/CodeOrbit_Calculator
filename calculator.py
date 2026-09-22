"""
Simple Calculator
CodeOrbit Tech - Python Programming Internship

Performs basic arithmetic operations (add, subtract, multiply, divide)
based on user input, with proper error handling for invalid input and
division by zero.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    return a / b


def get_number(prompt):
    """
    Prompt the user for a number, re-asking until valid input is given.
    Handles ValueError for non-numeric input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def get_choice():
    """Display the operation menu and return the user's validated choice."""
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1-5): ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return choice
        print("Invalid choice. Please enter a number from 1 to 5.")


def main():
    print("=== Simple Calculator ===")

    while True:
        choice = get_choice()

        if choice == "5":
            print("Goodbye!")
            break

        # Get the two operands from the user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)  # may raise ZeroDivisionError
                symbol = "/"

            print(f"\nResult: {num1} {symbol} {num2} = {result}\n")

        except ZeroDivisionError:
            # Handle division by zero gracefully instead of crashing
            print("\nError: Cannot divide by zero. Please try again.\n")


if __name__ == "__main__":
    main()