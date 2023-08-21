# ! Day16\project1\project1\Scripts\python.exe
from prettytable import PrettyTable

# Create a PrettyTable instance
table = PrettyTable()

# Define table columns
table.field_names = ["First Name", "Last Name", "Age", "Location"]

# Add rows to the table
table.add_row(["Firoz", "Mahmud", 25, "New York"])
table.add_row(["Maliha", "Rahman", 30, "Los Angeles"])
table.add_row(["Mollika", "Mubarak", 22, "Chicago"])

# Print the table
print(table)
