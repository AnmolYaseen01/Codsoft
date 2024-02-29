
# Contact Book Application

This Contact Book application is a simple yet effective GUI tool built using Tkinter in Python. It allows users to add, update, delete, and search contacts. Each contact consists of a name, phone number, email, and address. This README provides instructions on how to run and use the application.

## Features

- Add new contacts with name, phone, email, and address
- Update existing contacts
- Delete contacts
- Search for contacts by name
- Sort contacts by name, phone, email, or address
- Save contacts to a file
- Load contacts from a file

## Requirements

Before running the application, ensure you have Python installed on your system. This application has been tested with Python 3.8 and above.

## How to Run

1. Save the script to a file named `contact_book.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `contact_book.py` is saved.
4. Run the script with the command: `python contact_book.py`.

## Using the Application

### Main Interface

The main interface consists of input fields for the contact's details (Name, Phone, Email, Address), a list displaying all the contacts, and several buttons for different operations.

### Adding a Contact

1. Enter the contact's details in the corresponding fields.
2. Click the 'Add Contact' button.
3. The new contact will appear in the list.

### Updating a Contact

1. Select a contact from the list.
2. Modify the details in the input fields.
3. Click the 'Update Contact' button.

### Deleting a Contact

1. Select a contact from the list.
2. Click the 'Delete Contact' button.
3. Confirm the deletion.

### Searching for Contacts

1. Click the 'Search Contacts' button.
2. Enter a name or keyword in the prompt.
3. The list will update to show only matching contacts.

### Sorting Contacts

- Click on any column header (Name, Phone, Email, Address) to sort the contacts based on that column. Clicking again will toggle between ascending and descending order.

### Saving and Loading Contacts

- The application automatically saves contacts to `contacts.json` in the application's directory. Use the 'Load Contacts' option from the 'File' menu to load contacts from this file upon starting the application.

## About

The Contact Book App was created by Anmol Yaseen. It is intended for educational and small-scale personal use. For more information or to report issues, please refer to the contact information provided in the 'About' section of the application.

---

# Scientific Calculator Application

This Scientific Calculator is a versatile tool designed for both basic arithmetic and scientific calculations, featuring a user-friendly graphical interface built with Tkinter in Python. It supports operations such as addition, subtraction, multiplication, and division, along with scientific functions like sine, cosine, tangent, logarithms, and square root. This README details the steps for running the application and provides a guide on how to use its features.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Scientific functions: sine (`sin`), cosine (`cos`), tangent (`tan`), natural logarithm (`ln`), logarithm base 10 (`log`), and square root (`sqrt`).
- Memory functions: add to memory (`M+`), recall from memory (`MR`), and clear memory (`MC`).
- History panel to view previous calculations.
- Clear history functionality.
- User guide and about page for assistance.
- Keyboard input support for easier data entry.

## Requirements

To run the calculator, you need:

- Python 3.6 or newer installed on your computer.

## How to Run

1. Save the script to a file, for instance, `scientific_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the command: `python scientific_calculator.py`.

## Using the Application

### Basic Operations

Enter numbers and operation symbols (`+`, `-`, `*`, `/`) using the graphical buttons or your keyboard, then press `=` to calculate.

### Scientific Functions

Enter the number first, then click the function button (e.g., `sin`, `cos`, `tan`, `ln`, `log`, `sqrt`) to apply the scientific operation.

### Memory Functions

- `M+` adds the current display value to memory.
- `MR` recalls the value stored in memory to the display.
- `MC` clears the stored memory value.

### History Panel

The history panel on the right side of the application window shows your past calculations. Use the `Clear History` button to reset this panel.

### User Guide and About

Access the `Help` menu for a detailed user guide and information about the calculator.

## About

Developed by Anmol Yaseen, this Scientific Calculator application aims to provide a comprehensive calculation tool for educational, professional, and personal use. Enjoy the blend of simplicity and functionality for your calculation needs.

---

# Password Generator Application

The Password Generator is a Python application designed to help users create strong and secure passwords. Built with Tkinter, this GUI application offers customizable options for password complexity, including the ability to include lowercase letters, uppercase letters, numbers, and special characters. This README provides instructions on how to run the application and a brief guide on its features.

## Features

- Generate secure passwords based on user-selected criteria.
- Customize password length and inclusion of lowercase letters, uppercase letters, numbers, and special characters.
- Copy generated passwords to the clipboard for easy use.
- Accessible user guide and about page within the application.
- Simple, user-friendly interface.

## Requirements

To run the application, ensure you have Python installed on your system. This application has been developed and tested with Python 3.6 and above.

## How to Run

1. Save the script to a file named `password_generator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `password_generator.py` is saved.
4. Execute the script with the command: `python password_generator.py`.

## Using the Application

### Generating a Password

1. Enter the desired password length in the 'Password Length' field.
2. Select the character types to include in the password: lowercase letters, uppercase letters, numbers, and/or special characters.
3. Click the 'Generate Password' button to generate the password.
4. The generated password will be displayed below the button.

### Copying the Password

- Click the 'Copy to Clipboard' button to copy the generated password for easy use elsewhere.

### Accessing the User Guide and About Page

- Use the 'Help' menu at the top of the application to access the User Guide and About page for more information on how to use the application and its features.

## About

Developed by Anmol Yaseen, this Password Generator application aims to provide a simple yet effective tool for generating secure passwords. The application is intended for personal use and educational purposes.

---

# Rock-Paper-Scissors Game

This Rock-Paper-Scissors game is a simple, interactive Python application built with Tkinter. It allows players to compete against the computer in the classic game, with scores updated after each round. This README provides instructions on how to run the game and details its features.

## Features

- Play Rock-Paper-Scissors against the computer.
- Animated choices for user and computer selections.
- Score tracking for both player and computer.
- Ability to reset the game at any time.
- User guide and about information accessible from within the game.
- Simple and intuitive graphical user interface.

## Requirements

To run the game, you'll need:

- Python installed on your computer. The game has been developed and tested with Python 3.6 and above.

## How to Run

1. Save the script to a file, for instance, `rock_paper_scissors.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `rock_paper_scissors.py` is saved.
4. Run the script with the command: `python rock_paper_scissors.py`.

## How to Play

1. **Start the Game:** Open the game as described above. The main window will display the game's title and current round number, along with score trackers for both the player and the computer.

2. **Make Your Choice:** Select "Rock", "Paper", or "Scissors" from the dropdown menu. 

3. **Play a Round:** Click the 'Play' button to play a round. The game will animate selections, display both the player's and computer's choices, and then show the result of the round.

4. **Continue Playing:** After each round, the scores are updated accordingly, and you can continue playing by making another selection and clicking 'Play' again.

5. **Reset the Game:** Click the 'Reset' button at any time to start a new game. This resets the scores and round number.

## Additional Features

- **User Guide:** Access the user guide from the 'Help' menu for information on playing the game.

- **About:** Find out more about the game and its creator from the 'About' option in the 'Help' menu.

## About

Developed by Anmol Yaseen, this Rock-Paper-Scissors game is a fun, interactive way to enjoy the classic game with a modern twist. It's perfect for quick breaks or to practice decision-making skills.

---

# To-Do Application

This To-Do Application is a versatile tool designed to help users manage tasks efficiently. Built with Tkinter in Python, it features functionalities such as adding, editing, deleting tasks, marking tasks as completed, and exporting tasks to a CSV file. This README provides instructions on how to run the application and a guide on its features.

## Features

- Add tasks with details such as task name, category, priority, details, and due date.
- Edit existing tasks to update any details.
- Delete tasks from the list.
- Export tasks to a CSV file for external use.
- Mark tasks as completed and track completion dates.
- Filter tasks based on category, priority, or completion status.
- Automatically save tasks upon closing and load them when reopening the application.
- Shortcut keys for quick access to functionalities.

## Requirements

To run the application, ensure you have Python installed on your computer. This application has been developed and tested with Python 3.6 and above.

## How to Run

1. Save the script to a file named `todo_app.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `todo_app.py` is saved.
4. Run the script with the command: `python todo_app.py`.

## Using the Application

### Main Interface

The main interface consists of input fields for task details (Task, Category, Priority, Details, Due Date), a list displaying all tasks, and several buttons for different operations.

### Adding a Task

1. Enter the task's details in the corresponding fields.
2. Click the 'Add Task' button or press `Ctrl+N` to save the task.

### Editing a Task

1. Select a task from the list.
2. Modify the task's details in the input fields.
3. Click the 'Edit Task' button or press `Ctrl+E` to save the changes.

### Deleting a Task

1. Select a task from the list.
2. Click the 'Delete Task' button or press the `Delete` key to remove the task.

### Exporting Tasks to CSV

- Click the 'Export to CSV' button to save the current list of tasks to a CSV file. You will be prompted to choose a save location.

### Marking a Task as Completed

- Select one or more tasks from the list, then click the 'Mark as Completed' button or press `Ctrl+M` to mark the selected tasks as completed.

### Applying Filters

- Use the 'Filter by:' dropdown to select a filter category (Category, Priority, Completed), enter a filter value in the adjacent text field, and click 'Search' to filter tasks.

### Accessing the User Guide

- Use the 'Help' menu at the top of the application to access the User Guide for more information on how to use the application and its features.

## About

Developed by Anmol Yaseen, this To-Do Application aims to provide a comprehensive solution for task management. The application is intended for personal use and educational purposes.

---

