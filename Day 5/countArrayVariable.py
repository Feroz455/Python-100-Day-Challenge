heights = [int(height) for height in input(
    "Enter list of student heights in meters separated by spaces: ").split()]
count = 0
sum = 0
for height in heights:
    sum += height
    count += 1

print(f"Average = {sum/count}")
