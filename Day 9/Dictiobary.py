# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])

# Modifying values
student["age"] = 21
student["major"] = "Data Science"

# Adding new key-value pairs
student["gpa"] = 3.8

# Removing a key-value pair
del student["major"]

# Checking if a key exists in the dictionary
if "gpa" in student:
    print("GPA:", student["gpa"])

# Getting all keys and values
keys = student.keys()
values = student.values()

# Iterating through keys and values
for key, value in student.items():
    print(key, ":", value)
