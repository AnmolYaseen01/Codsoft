import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime
import csv

class Task:
    def __init__(self, name, category, priority, details, due_date, completed=False, completed_date=""):
        self.name = name
        self.category = category
        self.priority = priority
        self.details = details
        self.due_date = due_date
        self.completed = completed
        self.completed_date = completed_date

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do App")
        self.geometry("900x600")
        self.tasks = []
        self.load_tasks()
        self.initialize_ui()

    def initialize_ui(self):
        self.create_menu()

        # Create a frame to hold the input widgets
        input_frame = ttk.Frame(self)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(input_frame, text="Task:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.task_input = ttk.Entry(input_frame, width=40)
        self.task_input.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Category:", font=("Helvetica", 12)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.category_var = tk.StringVar()
        self.category_entry = ttk.Entry(input_frame, textvariable=self.category_var, width=20)
        self.category_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Priority:", font=("Helvetica", 12)).grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.priority_var = tk.StringVar()
        self.priority_combobox = ttk.Combobox(input_frame, textvariable=self.priority_var, values=["High", "Medium", "Low"])
        self.priority_combobox.grid(row=0, column=5, padx=5, pady=5)
        self.priority_combobox.set("Medium")

        ttk.Label(input_frame, text="Details:", font=("Helvetica", 12)).grid(row=0, column=6, padx=5, pady=5, sticky="e")
        self.details_var = tk.StringVar()
        self.details_entry = ttk.Entry(input_frame, textvariable=self.details_var, width=30)
        self.details_entry.grid(row=0, column=7, padx=5, pady=5)

        ttk.Label(input_frame, text="Due Date:", font=("Helvetica", 12)).grid(row=0, column=8, padx=5, pady=5, sticky="e")
        self.due_date_var = tk.StringVar()
        self.due_date_entry = ttk.Entry(input_frame, textvariable=self.due_date_var, width=15)
        self.due_date_entry.grid(row=0, column=9, padx=5, pady=5)
        self.due_date_entry.insert(0, self.get_current_datetime())

        ttk.Button(input_frame, text="Add Task", command=self.add_task).grid(row=0, column=10, padx=5, pady=5)

        # Create a frame to hold the treeview and buttons
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        columns = ("Task", "Category", "Priority", "Details", "Due Date", "Completed", "Completed Date")
        self.task_treeview = ttk.Treeview(tree_frame, columns=columns, selectmode="extended")
        self.task_treeview.grid(row=0, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

        for col in columns:
            self.task_treeview.heading(col, text=col, command=lambda c=col: self.sort_tasks(c))
            self.task_treeview.column(col, width=120, anchor="center")

        ttk.Button(tree_frame, text="Edit Task", command=self.edit_task).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(tree_frame, text="Delete Task", command=self.delete_task).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(tree_frame, text="Export to CSV", command=self.export_to_csv).grid(row=1, column=2, padx=5, pady=5)
        
        # Create the "Mark as Completed" button
        ttk.Button(tree_frame, text="Mark as Completed", command=self.mark_task_completed).grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(tree_frame, text="Total Tasks: 0").grid(row=1, column=4, padx=5, pady=5)
        ttk.Label(tree_frame, text="Completed Tasks: 0").grid(row=1, column=5, padx=5, pady=5)

        ttk.Label(tree_frame, text="Filter by:").grid(row=1, column=6, padx=5, pady=5, sticky="e")
        self.filter_var = tk.StringVar()
        filter_combobox = ttk.Combobox(tree_frame, textvariable=self.filter_var, values=["Category", "Priority", "Completed"])
        filter_combobox.grid(row=1, column=7, padx=5, pady=5)
        
        self.filter_entry_var = tk.StringVar()
        filter_entry = ttk.Entry(tree_frame, textvariable=self.filter_entry_var, width=15)
        filter_entry.grid(row=1, column=8, padx=5, pady=5)
        
        ttk.Button(tree_frame, text="Search", command=self.apply_filter).grid(row=1, column=9, padx=5, pady=5)

        self.update_task_list()
        self.update_task_count()

        # Configure grid rows and columns for resizing
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(10, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Register shortcut keys
        self.bind("<Control-n>", lambda event: self.add_task())
        self.bind("<Control-e>", lambda event: self.edit_task())
        self.bind("<Delete>", lambda event: self.delete_task())
        self.bind("<Control-s>", lambda event: self.save_tasks())
        self.bind("<Control-o>", lambda event: self.load_tasks())
        self.bind("<Control-m>", lambda event: self.mark_task_completed())

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Tasks", command=self.save_tasks)
        file_menu.add_command(label="Load Tasks", command=self.load_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create the "Help" menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="User Guide", command=self.show_user_guide)

    def add_task(self):
        name = self.task_input.get().strip()
        category = self.category_var.get().strip()
        priority = self.priority_var.get()
        details = self.details_var.get().strip()
        due_date = self.due_date_var.get().strip()

        if name:
            task = Task(name, category, priority, details, due_date)
            self.tasks.append(task)
            self.update_task_list()
            self.clear_task_input()
            self.update_task_count()
            messagebox.showinfo("Task Added", "Task added successfully.")
        else:
            messagebox.showwarning("Empty Task", "Task name cannot be empty.")

    def edit_task(self):
        selected_items = self.task_treeview.selection()
        if not selected_items:
            messagebox.showwarning("No Task Selected", "Please select a task to edit.")
            return

        selected_item = selected_items[0]
        index = int(selected_item.split('I')[1]) - 1
        selected_task = self.tasks[index]
        selected_task.name = self.task_input.get().strip()
        selected_task.category = self.category_var.get().strip()
        selected_task.priority = self.priority_var.get()
        selected_task.details = self.details_var.get().strip()
        selected_task.due_date = self.due_date_var.get().strip()

        self.update_task_list()
        self.clear_task_input()
        messagebox.showinfo("Task Updated", "Task updated successfully.")

    def delete_task(self):
        selected_items = self.task_treeview.selection()
        if not selected_items:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")
            return

        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
        if confirmed:
            for item in selected_items:
                self.task_treeview.delete(item)  # Delete the selected item from the Treeview
                task_index = int(item.split('I')[1]) - 1  # Extract and convert the index
                self.tasks.pop(task_index)  # Remove the task from the tasks list

            self.clear_task_input()
            self.update_task_count()
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")

    def apply_filter(self):
        filter_type = self.filter_var.get()
        filter_text = self.filter_entry_var.get().strip().lower()

        if filter_type == "category":
            filtered_tasks = [task for task in self.tasks if filter_text in task.category.lower()]
        elif filter_type == "priority":
            filtered_tasks = [task for task in self.tasks if filter_text == task.priority.lower()]
        elif filter_type == "completed":
            if filter_text == "yes":
                filtered_tasks = [task for task in self.tasks if task.completed]
            elif filter_text == "no":
                filtered_tasks = [task for task in self.tasks if not task.completed]
            else:
                filtered_tasks = self.tasks[:]
        else:
            filtered_tasks = self.tasks[:]

        self.update_task_list(filtered_tasks)

    def update_task_list(self, tasks=None):
        self.task_treeview.delete(*self.task_treeview.get_children())
        tasks = tasks if tasks else self.tasks
        for index, task in enumerate(tasks, start=1):
            completed_date = task.completed_date if task.completed else ""
            self.task_treeview.insert("", index, values=(
                task.name, task.category, task.priority, task.details, task.due_date,
                "Yes" if task.completed else "No", completed_date), iid=f"I{index}")

    def update_task_count(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        self.task_treeview.heading("Completed", text=f"Completed ({completed_tasks}/{total_tasks})")

    def sort_tasks(self, column):
        self.tasks.sort(key=lambda x: getattr(x, column).lower())
        self.update_task_list()

    def export_to_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["Task", "Category", "Priority", "Details", "Due Date", "Completed", "Completed Date"])
                    writer.writeheader()
                    for task in self.tasks:
                        writer.writerow(vars(task))
                messagebox.showinfo("Info", f"Tasks exported to {file_path}.")
            except Exception as e:
                messagebox.showerror("Error", f"Error while exporting tasks: {str(e)}")

    def clear_task_input(self):
        self.task_input.delete(0, tk.END)
        self.category_var.set("")
        self.priority_combobox.set("Medium")
        self.details_var.set("")
        self.due_date_var.set(self.get_current_datetime())

    def get_current_datetime(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                task_data = json.load(file)
                self.tasks = [Task(**data) for data in task_data]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        task_data = [vars(task) for task in self.tasks]
        with open("tasks.json", "w") as file:
            json.dump(task_data, file)

    def mark_task_completed(self):
        selected_items = self.task_treeview.selection()
        if not selected_items:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")
            return

        for item in selected_items:
            index = int(item.split('I')[1]) - 1
            task = self.tasks[index]
            task.completed = True
            task.completed_date = self.get_current_datetime()

        self.update_task_list()
        self.update_task_count()
        messagebox.showinfo("Task Completed", "Task marked as completed.")

    def show_user_guide(self):
        user_guide_window = tk.Toplevel(self)
        user_guide_window.title("User Guide")

        user_guide_text = """
        User Guide:
        -------------

        - Add Task: Enter task details and press Enter or click "Add Task."
        - Edit Task: Select a task from the list and press Ctrl+E or click "Edit Task."
        - Delete Task: Select a task from the list and press Delete or click "Delete Task."
        - Save Tasks: Press Ctrl+S to save tasks.
        - Load Tasks: Press Ctrl+O to load tasks.
        - Mark as Completed: Select one or more tasks and press Ctrl+M to mark as completed.

        Shortcut Keys:
        --------------
        - Ctrl+N: Add Task
        - Ctrl+E: Edit Task
        - Delete: Delete Task
        - Ctrl+S: Save Tasks
        - Ctrl+O: Load Tasks
        - Ctrl+M: Mark as Completed
        """

        user_guide_label = ttk.Label(user_guide_window, text=user_guide_text, font=("Helvetica", 12))
        user_guide_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = ToDoApp()
    app.protocol("WM_DELETE_WINDOW", app.save_tasks)
    app.mainloop()
