import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "YOUR_TOKEN"

def create_user(username):
    user_params = {
        "token": TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    return response.status_code

def update_user(username, new_username):
    user_endpoint = f"{PIXELA_ENDPOINT}/{username}"
    user_data = {
        "newUsername": new_username,
    }
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.put(url=user_endpoint, json=user_data, headers=headers)
    return response.status_code

def create_pixel(username, graph_id, quantity):
    current_date = datetime.now().strftime("%Y%m%d")
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    pixel_data = {"date": current_date, "quantity": str(quantity)}
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    return response.status_code

def create_user_button_clicked():
    username = username_entry.get()
    status_code = create_user(username)
    if status_code == 200:
        messagebox.showinfo("Success", "User created successfully.")
    else:
        messagebox.showerror("Error", f"Error: {status_code}")

def update_user_button_clicked():
    username = username_entry.get()
    new_username = new_username_entry.get()
    status_code = update_user(username, new_username)
    if status_code == 200:
        messagebox.showinfo("Success", "User updated successfully.")
    else:
        messagebox.showerror("Error", f"Error: {status_code}")

def create_pixel_button_clicked():
    username = username_entry.get()
    graph_id = graph_id_entry.get()
    quantity = quantity_entry.get()
    status_code = create_pixel(username, graph_id, quantity)
    if status_code == 200:
        messagebox.showinfo("Success", "Pixel created successfully.")
    else:
        messagebox.showerror("Error", f"Error: {status_code}")

# Create the main window
root = tk.Tk()
root.title("Pixela GUI")

# Use a ttk-themed style
style = ttk.Style()
style.theme_use("clam")

# Create and place themed widgets in the main window
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0)

username_label = ttk.Label(frame, text="Username:")
username_label.grid(column=0, row=0, padx=5, pady=5)
username_entry = ttk.Entry(frame)
username_entry.grid(column=1, row=0, padx=5, pady=5)
create_user_button = ttk.Button(frame, text="Create User", command=create_user_button_clicked)
create_user_button.grid(column=0, row=1, columnspan=2, pady=10)

new_username_label = ttk.Label(frame, text="New Username:")
new_username_label.grid(column=0, row=2, padx=5, pady=5)
new_username_entry = ttk.Entry(frame)
new_username_entry.grid(column=1, row=2, padx=5, pady=5)
update_user_button = ttk.Button(frame, text="Update User", command=update_user_button_clicked)
update_user_button.grid(column=0, row=3, columnspan=2, pady=10)

graph_id_label = ttk.Label(frame, text="Graph ID:")
graph_id_label.grid(column=0, row=4, padx=5, pady=5)
graph_id_entry = ttk.Entry(frame)
graph_id_entry.grid(column=1, row=4, padx=5, pady=5)
quantity_label = ttk.Label(frame, text="Quantity:")
quantity_label.grid(column=0, row=5, padx=5, pady=5)
quantity_entry = ttk.Entry(frame)
quantity_entry.grid(column=1, row=5, padx=5, pady=5)
create_pixel_button = ttk.Button(frame, text="Create Pixel", command=create_pixel_button_clicked)
create_pixel_button.grid(column=0, row=6, columnspan=2, pady=10)

root.mainloop()
