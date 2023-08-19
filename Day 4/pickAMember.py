import random
member = []


for i in range(10):
    name = input("Enter a name: ")
    member.append(name)  # Add the input name to the 'member' list

print("List of names:")
for name in member:
    print(name)
print(f"Bill will be paid by: {member[random.randint(0,9)]}")
