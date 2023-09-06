import pandas as pd

# Read data from the CSV file into a DataFrame
csv_file = "venv/Include/NATO-alphabet-start/nato_phonetic_alphabet.csv"
data_frame = pd.read_csv(csv_file)

# # Convert the DataFrame to a list of dictionaries
data = {row.letter:row.code for index, row in data_frame.iterrows()}

print(data)
# Iterate through the rows of the DataFrame
# for index, row in data_frame.iterrows():
#     print(f"Row index: {index}")
#     print(f"Data in this row:")
#     print(row)
#     print()  # Add a newline for separation

name = list(input("What is your name\t").upper())

result = { i : data[i] for i in name}
# for i in name:
#     print(data[i])
#     result[i] = data[i]

print(result)

# # Convert the DataFrame to a list of dictionaries
# data = data_frame.to_dict(orient='records')

# # Print the resulting dictionary
# print(data)

# # Access the keys of the first dictionary in the list
# if data:
#     keys = list(data[0].keys())
#     print(keys)
# else:
#     print("No data in the list.")



# for raw in data:
#     for key,value in raw.items():
#         print(f"{key} {value}")