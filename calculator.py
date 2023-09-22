import tkinter as tk
from tkinter import ttk
import math

# Global variables
current_input = ""
memory = 0
ans = None
scientific_mode = False
history = []

def handle_error():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "Error")

def button_click(event):
    global current_input, ans

    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_input)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            ans = result
            add_to_history(current_input, result)
        except ZeroDivisionError:
            handle_error()
            entry.insert(tk.END, "Division by Zero")
        except Exception as e:
            handle_error()
            entry.insert(tk.END, str(e))
        current_input = ""
    elif button_text == "C":
        entry.delete(0, tk.END)
        current_input = ""
    elif button_text == "CE":
        entry.delete(0, tk.END)
    elif button_text == "M+":
        try:
            global memory
            memory += float(entry.get())
            current_input = ""
        except Exception as e:
            handle_error()
    elif button_text == "MR":
        entry.delete(0, tk.END)
        entry.insert(tk.END, memory)
        current_input = ""
    elif button_text == "ANS":
        if ans is not None:
            current_input += str(ans)
            entry.insert(tk.END, str(ans))
    elif button_text == "⌫":
        current_input = current_input[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_input)
    else:
        current_input += button_text
        entry.insert(tk.END, button_text)

def add_to_history(calculation, result):
    history.append((calculation, result))
    update_history_panel()

def clear_history():
    global history
    history = []
    update_history_panel()

def update_history_panel():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    for i, (calculation, result) in enumerate(history, start=1):
        history_text.insert(tk.END, f"{i}. {calculation} = {result}\n")
    history_text.config(state=tk.DISABLED)

def toggle_calculator_mode():
    global scientific_mode
    scientific_mode = not scientific_mode
    configure_buttons()

def configure_buttons():
    if scientific_mode:
        basic_frame.grid_forget()
        scientific_frame.grid(row=1, column=0, columnspan=5)  # Adjust columnspan
        calculator_mode_button.config(text="Switch to Basic")
    else:
        scientific_frame.grid_forget()
        basic_frame.grid(row=1, column=0, columnspan=4)  # Adjust columnspan
        calculator_mode_button.config(text="Switch to Scientific")

def on_key(event):
    key = event.char
    if key in "0123456789.+-*/()":
        if scientific_mode:
            scientific_button_click(tk.Event(widget=None, char=key))
        else:
            button_click(tk.Event(widget=None, char=key))

def clear_memory():
    global memory
    memory = 0

def store_memory():
    global memory
    try:
        memory = float(entry.get())
    except Exception as e:
        handle_error()

def clear_history_window():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    history_text.config(state=tk.DISABLED)

def scientific_button_click(event):
    button_text = event.widget.cget("text")

    if button_text in ["sin", "cos", "tan", "ln", "log", "sqrt"]:
        try:
            value = float(entry.get())
            if button_text == "sin":
                result = math.sin(math.radians(value))
            elif button_text == "cos":
                result = math.cos(math.radians(value))
            elif button_text == "tan":
                result = math.tan(math.radians(value))
            elif button_text == "ln":
                result = math.log(value)
            elif button_text == "log":
                result = math.log10(value)
            elif button_text == "sqrt":
                result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            handle_error()

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a styled theme for ttk buttons
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 14))

# Create the entry field with improved styling
entry = tk.Entry(root, width=20, font=('Helvetica', 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

# Create frames for basic and scientific calculator buttons
basic_frame = ttk.Frame(root)
scientific_frame = ttk.Frame(root)

# Define button labels for the main calculator
main_button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'CE', 'M+', 'MR', '⌫'
]

# Create and arrange main calculator ttk buttons
row_val = 1
col_val = 0
main_buttons = []

for label in main_button_labels:
    button = ttk.Button(basic_frame, text=label)
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", button_click)
    main_buttons.append(button)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Create a button to toggle calculator mode
calculator_mode_button = ttk.Button(root, text="Switch to Scientific", command=toggle_calculator_mode)
calculator_mode_button.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

# Create a history panel
history_panel = ttk.LabelFrame(root, text="History")
history_panel.grid(row=1, column=4, rowspan=6, padx=10, pady=10, sticky="nsew")

history_text = tk.Text(history_panel, height=10, width=30, wrap=tk.WORD)
history_text.pack(fill=tk.BOTH, expand=True)
history_text.config(state=tk.DISABLED)

# Create a clear history button
clear_history_button = ttk.Button(history_panel, text="Clear History", command=clear_history)
clear_history_button.pack()

# Define button labels for the scientific calculator
scientific_button_labels = [
    'sin', 'cos', 'tan', 'ln', 'log',
    'sqrt', 'sinh', 'cosh', 'tanh', 'x²'
]

# Create scientific calculator ttk buttons (not visible initially)
row_val = 1
col_val = 0
scientific_buttons = []

for label in scientific_button_labels:
    button = ttk.Button(scientific_frame, text=label)
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", scientific_button_click)
    scientific_buttons.append(button)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Configure button visibility based on initial calculator mode
configure_buttons()

# Allow resizing the window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Bind keyboard events
root.bind("<Key>", on_key)

# Run the Tkinter main loop
root.mainloop()
