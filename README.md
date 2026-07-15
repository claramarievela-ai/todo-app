# To-Do List App

A simple command-line To-Do List application built in Python. This project 
was built to practice core Python fundamentals: control structures, 
functions, user input handling, and error handling with try/except/else/finally.

## Features

- Add tasks to your list
- View all current tasks
- Delete a task by number
- Exit the application
- Handles invalid input gracefully (non-numeric input, out-of-range task 
  numbers, invalid menu choices, and empty task lists)

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository: https://github.com/claramarievela-ai/todo-app.git
3. Navigate into the project folder and run: python3 menu.py

## How to Use
When the app starts, you'll see a menu:
To-Do List

Add a task
View tasks
Delete a task
Exit

- Type `1` to add a new task
- Type `2` to view your current tasks
- Type `3` to delete a task by entering its number
- Type `4` to exit the app

The app will alert you if you enter an invalid menu option, try to view or 
delete tasks when your list is empty, or try to delete a task number that 
doesn't exist.
