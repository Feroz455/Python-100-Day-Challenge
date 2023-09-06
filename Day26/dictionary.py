import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student = {name: random.randint(1, 100) for name in names}
print(student)