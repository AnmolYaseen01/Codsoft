import tkinter as tk
import random
import string
from tkinter import messagebox

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
        result_label.config(text="Please select at least one character type.", fg="red", font=("Helvetica", 10))
    else:
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text=generated_password, fg="green", font=("Helvetica", 12, "bold"))

# Function to open the user guide
def open_user_guide():
    user_guide = tk.Toplevel()
    user_guide.title("User Guide")

    user_guide_text = """
    User Guide:
    - Enter the desired password length in the 'Password Length' field.
    - Check the options you want to include in the password.
    - Click the 'Generate Password' button to generate a password.
    - You can click 'Copy to Clipboard' to copy the generated password.
    """

    user_guide_label = tk.Label(user_guide, text=user_guide_text, font=("Helvetica", 12))
    user_guide_label.pack(padx=20, pady=20)

# Function to open the about page
def open_about_page():
    about_page = tk.Toplevel()
    about_page.title("About")

    about_text = """
    Password Generator v1.0
    Created by Anmol Yaseen
    Copyright © 2023

    This password generator helps you create secure passwords
    with various character options.
    """

    about_label = tk.Label(about_page, text=about_text, font=("Helvetica", 12))
    about_label.pack(padx=20, pady=20)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x500")  # Set window dimensions

# Create a frame for better organization
frame = tk.Frame(window, padx=20, pady=20, bg="#f0f0f0")  # Light gray background
frame.pack(expand=True, fill=tk.BOTH)

# Create a menu bar
menubar = tk.Menu(window)
window.config(menu=menubar)

# Add File menu to the menu bar
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.quit)

# Add Help menu to the menu bar
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="User Guide", command=open_user_guide)
help_menu.add_command(label="About", command=open_about_page)

# Title Label
title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=(0, 10))

# Password Length Label and Entry
length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
length_label.pack(anchor="w")

length_entry = tk.Entry(frame, font=("Helvetica", 12))
length_entry.pack(anchor="w", pady=(0, 10))

# Character Options Label
options_label = tk.Label(frame, text="Character Options:", font=("Helvetica", 12), bg="#f0f0f0")
options_label.pack(anchor="w", pady=(10, 5))

# Checkboxes for character options
lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(frame, text="Include Lowercase", variable=lowercase_var, font=("Helvetica", 10), bg="#f0f0f0")
lowercase_checkbox.pack(anchor="w")

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(frame, text="Include Uppercase", variable=uppercase_var, font=("Helvetica", 10), bg="#f0f0f0")
uppercase_checkbox.pack(anchor="w")

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var, font=("Helvetica", 10), bg="#f0f0f0")
numbers_checkbox.pack(anchor="w")

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(frame, text="Include Special Characters", variable=special_chars_var, font=("Helvetica", 10), bg="#f0f0f0")
special_chars_checkbox.pack(anchor="w")

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#007bff", fg="white", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=20)

# Label to display the generated password
result_label = tk.Label(frame, text="", wraplength=300, font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack(pady=(10, 20))

# Copy Button to copy the generated password to clipboard
copy_button = tk.Button(frame, text="Copy to Clipboard", command=generate_password, bg="#28a745", fg="white", font=("Helvetica", 12, "bold"))
copy_button.pack()

# Configure column and row weights to make the frame expand
frame.columnconfigure(1, weight=1)

# Start the GUI main loop
window.mainloop()
