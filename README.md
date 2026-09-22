# Simple Calculator

A command-line calculator built in Python as part of the CodeOrbit Tech Python Programming Internship.

## Features

- **Basic operations**: Add, Subtract, Multiply, Divide
- **Extended operations**: Power (^), Square Root, Modulus (%)
- **Memory**: reuse your last result in the next calculation by typing `M` instead of a number
- **History**: view all calculations from the current session (menu option 8)
- **Error handling**: gracefully handles invalid input (non-numeric entries) and division/modulus by zero using `try`/`except`, instead of crashing
- **Clean output formatting**: results are rounded and shown without unnecessary decimal places

## How to run

```bash
python calculator.py
```

Follow the on-screen menu to choose an operation and enter your numbers.

## Example
Enter choice (1-9): 1
Enter first number (or 'M'): 10
Enter second number (or 'M'): 5

Result: 10 + 5 = 15

## Concepts demonstrated

- Functions and code organization
- Dictionaries used for operation lookup (instead of long if/elif chains)
- A class (`Calculator`) to manage state (memory, history)
- Exception handling (`ValueError`, `ZeroDivisionError`)
- Input validation and user-friendly CLI design
