# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox  # Import messagebox
import random
import string
from tkinter import *
import pyperclip  
import json  # Import the json module
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # Check if any entry is empty
    if not website or not email or not password:
        messagebox.showwarning("Warning", "Please fill in all fields before saving.")
        return
    try:
        with open("data.json", "r") as data_file:
            #reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            #saving update data
            json.dump(data, data_file, indent=4)
            # data_file.write(f"{website} | {email} | {password}\n")
    finally:  
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo("Success", "Password saved successfully!")



def generate_password():
    length = 16
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, END)  # Clear any existing text in the Entry
    password_entry.insert(0, password)  # Insert the generated password
    pyperclip.copy(password)

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo("Password Details", f"Website: {website}\nEmail: {email}\nPassword: {password}")
            else:
                messagebox.showwarning("Not Found", "No details for the website found in the database.")
    except FileNotFoundError:
        messagebox.showwarning("Not Found", "No data file found.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Create a canvas with a background color
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0,  )

# Entry fields
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="w" )
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"FirozMahmud@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="w", padx=3)

# Buttons
generator_button = Button(text="Generate Password", width=15, command=generate_password)
generator_button.grid(row=3, column=1, sticky="e", pady=10)
search = Button(text = "Search", width=15, command=search)
search.grid(row=1, column=1, sticky="e")
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



