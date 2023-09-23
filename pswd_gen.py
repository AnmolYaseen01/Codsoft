import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special_chars = special_chars_var.get()

    characters = ''
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if characters == '':
        result_label.config(text="Please select at least one character type.", fg="red")
    else:
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text=generated_password, fg="green")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a frame for better organization
frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

# Title Label
title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 18))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Password Length Label and Entry
length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=1, column=0, sticky="w")
length_entry = tk.Entry(frame)
length_entry.grid(row=1, column=1, sticky="e")

# Character Options Label
options_label = tk.Label(frame, text="Character Options:")
options_label.grid(row=2, column=0, columnspan=2, pady=(10, 5), sticky="w")

# Checkboxes for character options
lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(frame, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=3, column=0, columnspan=2, sticky="w")

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(frame, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=4, column=0, columnspan=2, sticky="w")

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=5, column=0, columnspan=2, sticky="w")

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(frame, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=6, column=0, columnspan=2, sticky="w")

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_button.grid(row=7, column=0, columnspan=2, pady=20)

# Label to display the generated password
result_label = tk.Label(frame, text="", wraplength=400, font=("Helvetica", 12))
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Configure column and row weights to make the frame expand
frame.columnconfigure(1, weight=1)
frame.rowconfigure(8, weight=1)

# Start the GUI main loop
window.mainloop()
