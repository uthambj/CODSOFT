# Task 1 — To-Do List Application

**CodSoft Python Programming Internship**

A command-line To-Do List manager built in Python. Users can add, view,
update, mark complete, and delete tasks. All tasks are stored persistently
in `data/tasks.json`, so nothing is lost between sessions.

## Features
- Add a task with a title and optional description
- View all tasks with their completion status
- Update a task's title or description
- Mark a task as complete
- Delete a task
- Persistent storage using JSON (no database setup required)

## Project Structure
```
Task1_ToDoList/
├── todo.py                 # Main application source code
├── data/
│   └── tasks.json           # Sample / persisted task data
├── outputs/
│   └── sample_run.txt       # Example of a terminal session
├── requirements.txt
└── README.md
```

## How to Run
```bash
python3 todo.py
```
No external dependencies are required — only the Python standard library.

## Example
```
==================================================
            TO-DO LIST APPLICATION
==================================================
1. Add Task
2. View Tasks
3. Update Task
4. Mark Task as Complete
5. Delete Task
6. Exit
==================================================
Choose an option (1-6): 1
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
Task 'Buy groceries' added successfully.
```

See `outputs/sample_run.txt` for a full example session.

