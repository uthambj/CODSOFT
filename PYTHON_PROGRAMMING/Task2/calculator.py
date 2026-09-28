"""
Simple Calculator Application
CodSoft Python Programming Internship - Task 2

Prompts the user for two numbers and an operator, performs the calculation,
and displays the result. Supports repeated calculations in a loop and
logs every calculation to outputs/calculation_log.txt.
"""

import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "outputs", "calculation_log.txt")


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")


def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 % num2
    elif operator == "**":
        return num1 ** num2
    else:
        raise ValueError("Unsupported operator.")


def log_result(num1, operator, num2, result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {num1} {operator} {num2} = {result}\n")


def main():
    print("=" * 45)
    print("           SIMPLE CALCULATOR")
    print("=" * 45)
    print("Supported operations: + - * / % ** (power)")
    print("Type 'q' at any time to quit.\n")

    while True:
        num1_input = input("Enter first number (or 'q' to quit): ").strip()
        if num1_input.lower() == "q":
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Invalid number. Please try again.\n")
            continue

        operator = input("Choose an operation (+, -, *, /, %, **): ").strip()

        num2 = get_number("Enter second number: ")

        try:
            result = calculate(num1, operator, num2)
            print(f"Result: {num1} {operator} {num2} = {result}\n")
            log_result(num1, operator, num2, result)
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Thank you for using the calculator. Goodbye!")


if __name__ == "__main__":
    main()
