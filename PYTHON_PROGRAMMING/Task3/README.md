"""
Password Generator Application
CodSoft Python Programming Internship - Task 3

Generates strong, random passwords of a user-specified length and
complexity (lowercase, uppercase, digits, symbols). Uses the `secrets`
module for cryptographically secure randomness. Generated passwords are
optionally saved to outputs/generated_passwords.txt.
"""

import os
import string
import secrets
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "outputs", "generated_passwords.txt")


def get_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 for reasonable security.")
                continue
            return length
        except ValueError:
            print("Please enter a valid whole number.")


def get_yes_no(prompt, default_yes=True):
    suffix = " (Y/n): " if default_yes else " (y/N): "
    answer = input(prompt + suffix).strip().lower()
    if answer == "":
        return default_yes
    return answer.startswith("y")


def build_character_pool(use_lower, use_upper, use_digits, use_symbols):
    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    return "".join(secrets.choice(pool) for _ in range(length))


def save_password(password, length):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] length={length} -> {password}\n")


def main():
    print("=" * 45)
    print("          PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        length = get_length()
        use_lower = get_yes_no("Include lowercase letters?")
        use_upper = get_yes_no("Include uppercase letters?")
        use_digits = get_yes_no("Include digits?")
        use_symbols = get_yes_no("Include symbols?", default_yes=False)

        pool = build_character_pool(use_lower, use_upper, use_digits, use_symbols)
        if not pool:
            print("You must select at least one character type. Try again.\n")
            continue

        password = generate_password(length, pool)
        print(f"\nGenerated Password: {password}\n")

        if get_yes_no("Save this password to outputs/generated_passwords.txt?"):
            save_password(password, length)
            print("Password saved.\n")

        if not get_yes_no("Generate another password?"):
            break

    print("Thank you for using the Password Generator!")


if __name__ == "__main__":
    main()
