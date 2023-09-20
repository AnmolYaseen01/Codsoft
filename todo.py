import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

# Create a list to store tasks
task_list = []

# Function to add a task to the list and update the listbox
def add_task():
    task_text = task_entry.get()
    description_text = description_entry.get()
    due_date = due_date_entry.get()
    if task_text:
        if due_date:
            task_text += f" (Due: {due_date})"
        if description_text:
            task_text += f"\nDescription: {description_text}"
        task_list.append(task_text)
        task_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)  # Clear the task entry field
        description_entry.delete(0, tk.END)  # Clear the description entry field
        due_date_entry.delete(0, tk.END)  # Clear the due date entry field
        show_info("Task Added", "Task added successfully.", "info")
    else:
        show_info("Input Required", "Please enter a task.", "warning")

# Function to delete the selected task from the list and listbox
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task_listbox.delete(index)
        del task_list[index]
        show_info("Task Deleted", "Selected task deleted.", "info")
    else:
        show_info("No Task Selected", "Please select a task to delete.", "warning")

# Function to list all tasks
def list_tasks():
    tasks = "\n\n".join(task_list) if task_list else "No tasks found."
    show_info("Task List", tasks, "info")

# Function to set a reminder for the selected task
def set_reminder():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task_text = task_list[index]
        reminder_date = reminder_entry.get()
        if reminder_date:
            task_text += f"\nReminder: {reminder_date}"
            task_list[index] = task_text
            task_listbox.delete(index)
            task_listbox.insert(index, task_text)
            reminder_entry.delete(0, tk.END)  # Clear the reminder entry field
            show_info("Reminder Set", "Reminder set for the task.", "info")
        else:
            show_info("Input Required", "Please enter a reminder date.", "warning")
    else:
        show_info("No Task Selected", "Please select a task to set a reminder.", "warning")

# Function to check for task reminders
def check_reminders():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    reminder_tasks = [task for task in task_list if f"(Reminder: {current_date})" in task]
    if reminder_tasks:
        reminder_message = "Reminders for today:\n" + "\n\n".join(reminder_tasks)
        show_info("Reminders", reminder_message, "info")
    else:
        show_info("Reminders", "No reminders for today.", "info")

# Function to display info message boxes
def show_info(title, message, style):
    if style == "info":
        messagebox.showinfo(title, message)
    elif style == "warning":
        messagebox.showwarning(title, message)

# Create the main GUI window
root = tk.Tk()
root.title("To-Do List")

# Create and configure labels for input fields with a modern design
label_font = ("Helvetica", 12)
bg_color = "#F5F5F5"  # Light Gray
fg_color = "#333333"  # Dark Gray

task_label = ttk.Label(root, text="Task:", background=bg_color, font=label_font, foreground=fg_color)
description_label = ttk.Label(root, text="Description:", background=bg_color, font=label_font, foreground=fg_color)
due_date_label = ttk.Label(root, text="Due Date (optional):", background=bg_color, font=label_font, foreground=fg_color)
reminder_label = ttk.Label(root, text="Reminder Date (optional):", background=bg_color, font=label_font, foreground=fg_color)

# Create and configure the task entry field with a placeholder
task_entry = ttk.Entry(root, width=30, font=label_font)
task_entry.insert(0, "Enter a task...")  # Placeholder text

# Create and configure the description entry field with a placeholder
description_entry = ttk.Entry(root, width=30, font=label_font)
description_entry.insert(0, "Enter a description (optional)...")  # Placeholder text

# Create and configure the due date entry field with a placeholder
due_date_entry = ttk.Entry(root, width=30, font=label_font)
due_date_entry.insert(0, "YYYY-MM-DD (optional)")  # Placeholder text

# Create and configure the Add Task button with an icon and modern colors
add_button = ttk.Button(root, text="Add Task", command=add_task, width=15, style="Accent.TButton")

# Create and configure the Delete Task button with an icon and modern colors
delete_button = ttk.Button(root, text="Delete Task", command=delete_task, width=15, style="Accent.TButton")

# Create and configure the List All Tasks button with an icon and modern colors
list_all_button = ttk.Button(root, text="List All Tasks", command=list_tasks, width=15, style="Accent.TButton")

# Create and configure the Set Reminder entry field with a placeholder
reminder_entry = ttk.Entry(root, width=30, font=label_font)
reminder_entry.insert(0, "YYYY-MM-DD (optional)")  # Placeholder text

# Create and configure the Set Reminder button with an icon and modern colors
set_reminder_button = ttk.Button(root, text="Set Reminder", command=set_reminder, width=15, style="Accent.TButton")

# Create and configure the Check Reminders button with an icon and modern colors
check_reminders_button = ttk.Button(root, text="Check Reminders", command=check_reminders, width=15, style="Accent.TButton")

# Create and configure the task listbox with a scrollbar
task_listbox = tk.Listbox(root, width=40, height=10, font=label_font, bg="#F0F8FF", selectbackground="#333333", borderwidth=1, relief="solid")
task_listbox_scrollbar = ttk.Scrollbar(root, orient="vertical", command=task_listbox.yview)
task_listbox.config(yscrollcommand=task_listbox_scrollbar.set)

# Grid layout for labels and input fields
task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
task_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
description_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
description_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)
due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
due_date_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)
add_button.grid(row=0, column=3, padx=5, pady=5)
delete_button.grid(row=1, column=3, padx=5, pady=5)
list_all_button.grid(row=2, column=3, padx=5, pady=5)
reminder_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
reminder_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=2)
set_reminder_button.grid(row=3, column=3, padx=5, pady=5)
check_reminders_button.grid(row=4, column=0, padx=10, pady=5)

# Grid layout for the task listbox and scrollbar
task_listbox.grid(row=5, column=0, padx=10, pady=5, columnspan=5, sticky="nsew")
task_listbox_scrollbar.grid(row=5, column=5, padx=0, pady=5, sticky="ns")

# Column and row weights for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.rowconfigure(5, weight=1)

# Create a custom style for buttons
style = ttk.Style()
style.configure("Accent.TButton", background="#007BFF", foreground="#000000", font=label_font, borderwidth=1, relief="solid")

# Run the Tkinter main event loop
root.mainloop()
