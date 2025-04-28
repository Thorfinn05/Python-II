import string
import random 
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip  # For copy to clipboard functionality

# Define colors for a modern UI
PRIMARY_COLOR = "#9b87f5"  # Purple
SECONDARY_COLOR = "#7E69AB"  # Secondary Purple
BG_COLOR = "#F5F5F7"  # Light background
TEXT_COLOR = "#1A1F2C"  # Dark text
ACCENT_COLOR = "#33C3F0"  # Sky Blue

upc = string.ascii_uppercase
lwc = string.ascii_lowercase
num = string.digits
sym = string.punctuation

def password(char, user_choices):
    pwd = ""
    if 1 in user_choices:
        pwd += upc
    if 2 in user_choices:
        pwd += lwc
    if 3 in user_choices:
        pwd += num
    if 4 in user_choices:
        pwd += sym
    if not pwd:
        return "Invalid selection"

    pwd_gen = "".join(random.choices(pwd, k=char))

    def isStrong():
        strength = {1: "Very Weak", 2: "Weak", 3: "Good", 4: "Strong", 5: "Very Strong"}
        if 1 <= char <= 4:
            strong = 1
        elif 5 <= char <= 7:
            strong = 2
        elif 8 <= char <= 9:
            strong = 3
        elif 10 <= char <= 11:
            strong = 4
        else:
            strong = 5
        if len(user_choices) == 1 and 5 <= char <= 25:
            return strength[strong - 1]
        else:
            return strength[strong]

    return f"Your {isStrong()} password is",pwd_gen

def generate_password():
    try:
        char = int(textbox.get('1.0', tk.END).strip())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    user_choices = []
    if chk_upc_var.get():
        user_choices.append(1)
    if chk_lwc_var.get():
        user_choices.append(2)
    if chk_num_var.get():
        user_choices.append(3)
    if chk_sym_var.get():
        user_choices.append(4)

    strength_result, pwd_result = password(char, user_choices)
    if pwd_result:
        password_entry.delete(0, tk.END)
        result_label.config(text = strength_result)
        password_entry.insert(0, pwd_result)
        copy_label.config(text = "You can now copy & paste it 🥰")
        
def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        pyperclip.copy(pwd)
        copy_label.config(text="Password copied to clipboard! ✅", fg=ACCENT_COLOR)
    else:
        copy_label.config(text="No password to copy! ❌", fg="red")

# GUI setup with modern styling
root = tk.Tk()
root.title("Password Generator")
root.configure(bg=BG_COLOR)
root.geometry("700x600")  # Set window size

# Create a main frame
main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# Title with modern styling
title_label = tk.Label(
    main_frame, 
    text="Secure Password Generator", 
    font=('Arial', 24, 'bold'), 
    bg=BG_COLOR, 
    fg=PRIMARY_COLOR
)
title_label.pack(padx=20, pady=20)

# Subtitle
subtitle = tk.Label(
    main_frame,
    text="Create strong passwords for your online accounts",
    font=('Arial', 14),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
subtitle.pack(pady=10)

# Input frame
input_frame = tk.Frame(main_frame, bg=BG_COLOR)
input_frame.pack(pady=15)

# Length label and input with modern styling
tk.Label(
    input_frame, 
    text="Password Length (1-50):", 
    font=('Arial', 16), 
    bg=BG_COLOR, 
    fg=TEXT_COLOR
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Use a spinbox for better number input
length_var = tk.IntVar(value=12)
length_spinbox = ttk.Spinbox(
    input_frame, 
    from_=1, 
    to=50, 
    textvariable=length_var, 
    font=('Arial', 16),
    width=5
)
length_spinbox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Checkbox frame with modern styling
chk_frame = tk.LabelFrame(main_frame, text="Include:", font=('Arial', 14, 'bold'), bg=BG_COLOR, fg=SECONDARY_COLOR, padx=10, pady=10)
chk_frame.pack(fill="x", padx=20, pady=15)

# Checkbox variables
chk_upc_var = tk.IntVar(value=1)
chk_lwc_var = tk.IntVar(value=1)
chk_num_var = tk.IntVar(value=1)
chk_sym_var = tk.IntVar(value=1)

# Style the checkbuttons
chk_style = ttk.Style()
chk_style.configure("TCheckbutton", background=BG_COLOR, font=('Arial', 14))

# Create checkbuttons with better spacing
ttk.Checkbutton(chk_frame, text="Uppercase (A-Z)", variable=chk_upc_var, style="TCheckbutton").grid(row=0, column=0, padx=20, pady=10, sticky="w")
ttk.Checkbutton(chk_frame, text="Lowercase (a-z)", variable=chk_lwc_var, style="TCheckbutton").grid(row=0, column=1, padx=20, pady=10, sticky="w")
ttk.Checkbutton(chk_frame, text="Numbers (0-9)", variable=chk_num_var, style="TCheckbutton").grid(row=1, column=0, padx=20, pady=10, sticky="w")
ttk.Checkbutton(chk_frame, text="Symbols (!@#$)", variable=chk_sym_var, style="TCheckbutton").grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Button style
btn_style = ttk.Style()
btn_style.configure("Generate.TButton", font=('Arial', 16, 'bold'))

# Generate button
generate_btn = ttk.Button(
    main_frame, 
    text="Generate Password", 
    command=generate_password,
    style="Generate.TButton"
)
generate_btn.pack(pady=20)

# Result frame
result_frame = tk.Frame(main_frame, bg=BG_COLOR, pady=10)
result_frame.pack(fill="x")

# Strength indicator label
result_label = tk.Label(
    result_frame, 
    text="", 
    font=('Arial', 16, 'bold'),
    bg=BG_COLOR,
    fg=SECONDARY_COLOR
)
result_label.pack(pady=10)

# Password display frame
password_frame = tk.Frame(main_frame, bg=BG_COLOR, padx=10, pady=10, bd=2, relief="groove")
password_frame.pack(fill="x", padx=20)

# Password entry with monospace font for better readability
password_entry = tk.Entry(
    password_frame, 
    font=('Consolas', 16), 
    width=40, 
    justify='center',
    bd=0
)
password_entry.pack(fill="x", padx=10, pady=10)

# Copy button
copy_btn = ttk.Button(
    password_frame, 
    text="Copy to Clipboard", 
    command=copy_to_clipboard
)
copy_btn.pack(pady=10)

# Status label
copy_label = tk.Label(
    main_frame, 
    text="", 
    font=('Arial', 14),
    bg=BG_COLOR
)
copy_label.pack(pady=10)

# Function to update the generate_password function to use the spinbox
def modified_generate_password():
    try:
        char = length_var.get()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    user_choices = []
    if chk_upc_var.get():
        user_choices.append(1)
    if chk_lwc_var.get():
        user_choices.append(2)
    if chk_num_var.get():
        user_choices.append(3)
    if chk_sym_var.get():
        user_choices.append(4)

    if not user_choices:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return
        
    strength_result, pwd_result = password(char, user_choices)
    
    if pwd_result:
        password_entry.delete(0, tk.END)
        result_label.config(text=strength_result)
        
        # Set color based on strength
        if "Very Strong" in strength_result:
            result_label.config(fg="dark green")
        elif "Strong" in strength_result:
            result_label.config(fg="green")
        elif "Good" in strength_result:
            result_label.config(fg="orange")
        elif "Weak" in strength_result:
            result_label.config(fg="red")
        elif "Very Weak" in strength_result:
            result_label.config(fg="dark red")
            
        password_entry.insert(0, pwd_result)
        copy_label.config(text="Password ready to copy!", fg=PRIMARY_COLOR)

# Replace the old command with the new function
generate_btn.config(command=modified_generate_password)

# Center window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Start the application
root.mainloop()
