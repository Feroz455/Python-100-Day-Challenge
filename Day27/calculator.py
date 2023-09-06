import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry field for displaying the input and results
entry = tk.Entry(window, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons for numbers and operations
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Create and place buttons on the grid
row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == "=":
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 16), command=button_equal).grid(row=row_val, column=col_val)
    elif button_text == "C":
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 16), command=button_clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 16), command=lambda num=button_text: button_click(num)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the application
window.mainloop()
