import random
input_string = input("Enter comma-separated values: ")
input_list = input_string.split(',')
len = len(input_list)

print("List:", input_list)
print(f"Bill will be paid by: {input_list[random.randint(0,len)]}")
