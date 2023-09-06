# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("Nato/nato_phonetic_alphabet.csv")
# #TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        word = input("Enter a word (characters only): ").upper()
        if not word.isalpha():
            raise ValueError("Invalid input. Please enter a word with characters only.")
    except ValueError as e:
        print(e)
    else:
        break  # Exit the loop if valid input is provided


output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
