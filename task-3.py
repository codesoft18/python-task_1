import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Low":
        chars = string.ascii_letters + string.digits
    elif complexity == "Medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(chars) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create entry widget for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create a dropdown menu for password complexity
complexity_var = tk.StringVar(root)
complexity_var.set("Low")  # default value
complexity_label = tk.Label(root, text="Select password complexity:")
complexity_label.pack(pady=5)
complexity_menu = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_menu.pack(pady=5)

# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

# Create a label to display the generated password
password_label = tk.Label(root)
password_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
