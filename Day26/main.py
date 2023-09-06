number = [1,2,3]
new_number = [n+1 for n in number]
print(new_number)


tempNumber = [1,2,3,4,5]
new_TempNumber= [n*5 for n in range(1,5)]
print(new_TempNumber)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
four_letter_names = [name.upper() for name in names if len(name) == 4 ]
print(four_letter_names)
