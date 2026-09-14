"""
Calculator Main Entry Point Module

This module serves as the primary executable entry point for the Calculator Application.
It parses command-line arguments to launch either the graphical user interface (GUI)
or the interactive command-line interface (CLI) mode.
"""

import sys
from gui import ModernCalculatorGUI
import calculator


def run_cli():
    """
    Execute the interactive Command-Line Interface (CLI) calculator loop.

    Prompts the user sequentially for operands and operators, evaluates arithmetic
    expressions using calculator.py, and displays formatted results until exited.
    """
    print("--- CALCULATOR (CLI Mode) ---")
    start = True

    # Main outer loop to manage calculation sessions
    while start:
        try:
            # Prompt for initial numbers and operation
            number1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            number2 = float(input("Enter second number: "))

            # Route to mathematical module operations
            if operator == "+":
                result = calculator.add(number1, number2)
            elif operator == "-":
                result = calculator.sub(number1, number2)
            elif operator == "*":
                result = calculator.mult(number1, number2)
            elif operator == "/":
                try:
                    result = calculator.div(number1, number2)
                except ZeroDivisionError:
                    result = number1
                    print("Error: Division by zero is not allowed.")
            else:
                result = number1
                print("Invalid operator.")

            # Display evaluated result
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid operation.")

            # Inner loop for chaining subsequent calculations onto existing result
            while True:
                operator = input("Enter operator (+, -, *, /, =): ")

                # If operator is not equals (=), continue chaining calculations
                if operator != '=':
                    number = float(input("Enter number: "))
                    if operator == "+":
                        result = calculator.add(result, number)
                    elif operator == "-":
                        result = calculator.sub(result, number)
                    elif operator == "*":
                        result = calculator.mult(result, number)
                    elif operator == "/":
                        try:
                            result = calculator.div(result, number)
                        except ZeroDivisionError:
                            print("Error: Division by zero is not allowed.")
                    
                    if result is not None:
                        print(f"Result: {result}")
                    else:
                        print("Invalid operation.")
                else:
                    # Print final evaluation result and terminate session
                    print(f"Final Result: {result}")
                    print("Exiting the calculator.")
                    start = False
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    # Check command-line arguments to determine execution mode
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        # Launch console CLI mode
        run_cli()
    else:
        # Launch graphical GUI application loop
        app = ModernCalculatorGUI()
        app.mainloop()
