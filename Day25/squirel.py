import pandas


data = pandas.read_csv("./Central_Park_Squirrel_Census_Squirrel_Data.csv")

squirrel = data["Primary Fur Color"]
counts = squirrel.value_counts()

csv_file_path = 'sample_pandas.csv'
counts.to_csv(csv_file_path)
print(f'CSV file "{csv_file_path}" created successfully.')
