# Task 2 — Calculator Application

**CodSoft Python Programming Internship**

A simple command-line calculator that prompts the user for two numbers and
an operator, performs the calculation, and displays the result. Supports
repeated calculations in a single session and logs every calculation to
`outputs/calculation_log.txt`.

## Features
- Basic arithmetic: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`)
- Extras: modulus (`%`) and exponentiation (`**`)
- Input validation (rejects non-numeric input, handles divide-by-zero gracefully)
- Loops so the user can perform multiple calculations without restarting
- Automatic logging of every calculation with a timestamp

## Project Structure
```
Task2_Calculator/
├── calculator.py            # Main application source code
├── outputs/
│   └── calculation_log.txt  # Auto-generated log of past calculations
├── requirements.txt
└── README.md
```

## How to Run
```bash
python3 calculator.py
```
No external dependencies are required — only the Python standard library.

## Example
```
Enter first number (or 'q' to quit): 12
Choose an operation (+, -, *, /, %, **): +
Enter second number: 8
Result: 12.0 + 8.0 = 20.0
```

## Author
Prashanth S N — CodSoft Virtual Internship (Python Programming), Sept 2026
