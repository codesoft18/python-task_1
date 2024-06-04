import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets for numbers
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create a dropdown menu for operation selection
operation_var = tk.StringVar(root)
operation_var.set("+")  # default value
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack(pady=5)

# Create a button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root)
result_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
