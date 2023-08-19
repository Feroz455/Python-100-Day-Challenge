import random
# Generate and print 10 random integers
for i in range(10):
    random_integer = random.randint(1, 10)
    print(random_integer)

print()  # Add an empty line between the two sets of random numbers

# Generate and print 10 random floating-point numbers
for i in range(10):
    random_float = random.uniform(5, 10)
    print(random_float)
