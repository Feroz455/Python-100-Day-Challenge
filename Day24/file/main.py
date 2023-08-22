import os
# Read the list of names
with open("./file/invited_name.txt", "r") as file:
    contents = file.read()

name_list = contents.split("\n")

# Read the original letter
with open("./file/example.txt", "r") as file:
    letter = file.read()

# Create the 'letters' directory if it doesn't exist
letters_dir = "./letters"
if not os.path.exists(letters_dir):
    os.makedirs(letters_dir)

# Replace the placeholder and save modified letters
for name in name_list:
    new_letter = letter.replace("Aang", name)

    # Save each new letter in the 'letters' directory
    new_letter_filename = f"{letters_dir}/letter_to_{name}.txt"
    with open(new_letter_filename, "w") as new_letter_file:
        new_letter_file.write(new_letter)

    print(f"Letter for {name} saved as {new_letter_filename}")
