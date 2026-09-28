# Task 3 — Password Generator

**CodSoft Python Programming Internship**

A command-line password generator that creates strong, random passwords
using Python's `secrets` module (cryptographically secure, unlike `random`).
The user chooses the password length and which character sets to include.

## Features
- User-specified password length (minimum 4 characters)
- Toggle lowercase, uppercase, digits, and symbols independently
- Cryptographically secure randomness via `secrets.choice`
- Optionally save generated passwords to `outputs/generated_passwords.txt`
- Generate multiple passwords in one session

## Project Structure
```
Task3_PasswordGenerator/
├── password_generator.py         # Main application source code
├── outputs/
│   └── generated_passwords.txt   # Auto-generated saved passwords
├── requirements.txt
└── README.md
```

## How to Run
```bash
python3 password_generator.py
```
No external dependencies are required — only the Python standard library.

## Example
```
Enter desired password length (minimum 4): 12
Include lowercase letters? (Y/n): y
Include uppercase letters? (Y/n): y
Include digits? (Y/n): y
Include symbols? (y/N): y

Generated Password: e88I9hJ12E7a
```

## Author
Prashanth S N — CodSoft Virtual Internship (Python Programming), Sept 2026
