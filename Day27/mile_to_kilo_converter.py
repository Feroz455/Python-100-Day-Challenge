import tkinter as tk
from tkinter import ttk

def convert_miles_to_km():
    try:
        miles = float(miles_input.get())
        kilometers = miles * 1.60934
        kilometer_result_label.config(text=f"{kilometers:.2f} km")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.geometry("400x200")
window.resizable(False, False)

# Create a style for widgets
style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 12))
style.configure("TLabel", padding=5, font=("Arial", 12))

# Create and place widgets
frame = ttk.Frame(window)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Center-align columns and rows
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

miles_label = ttk.Label(frame, text="Miles:")
miles_label.grid(row=0, column=0, sticky="e")

miles_input = ttk.Entry(frame, width=10)
miles_input.grid(row=0, column=1)

calculate_button = ttk.Button(frame, text="Convert", command=convert_miles_to_km)
calculate_button.grid(row=1, columnspan=2, pady=10)

is_equal_label = ttk.Label(frame, text="Is equal to:")
is_equal_label.grid(row=2, column=0, sticky="e")

kilometer_result_label = ttk.Label(frame, text="0 km", font=("Arial", 14, "bold"))
kilometer_result_label.grid(row=2, column=1, sticky="w")

# Run the application
window.mainloop()
