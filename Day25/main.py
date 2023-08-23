
# import csv
# with open("./weather_data.csv", "r") as file:
#     data = file.read()


# lines = data.strip().split('\n')
# header = lines[0].split(',')
# weather_data = []

# for line in lines[1:]:
#     values = line.split(',')
#     day_data = {}
#     for i, value in enumerate(values):
#         day_data[header[i]] = value
#         print(day_data[header[i]])
#     weather_data.append(day_data)

# print(weather_data)
# weather_data = []

# # Read the CSV data using the csv.reader
# csv_reader = csv.reader(data.split('\n'))
# header = next(csv_reader)  # Read the first line as header

# # Iterate through the remaining rows and create dictionaries
# for row in csv_reader:
#     day_data = dict(zip(header, row))
#     weather_data.append(day_data)

# print(weather_data)
# # Extract temperature values into a separate list
# temperature_list = [int(day_data['temp']) for day_data in weather_data]
# day_list = [(day_data["day"]) for day_data in weather_data]
# print(temperature_list)
# print(day_list)
import pandas
data = pandas.read_csv("./weather_data.csv")
# weather_dictionary = data.to_dict()
# print(weather_dictionary)

# weather_list =
# print(data["temp"].median())
# max = data["temp"].max()
# print(data["temp"].max())
df = (data["temp"] * 9 / 5)+32
# print(data["temp"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
print(df)
