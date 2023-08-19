def prime(number):
    for i in range(2, number):
        if (number % i == 0):
            return 0
    return 1


temp = int(input("Enter your number:\t"))
if (prime(temp)):
    print("Prime")
else:
    print("Not prime")
