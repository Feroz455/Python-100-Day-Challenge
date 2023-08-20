from Art import hammer
import os
import random


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


bidding = {}
isFinished = False

while not isFinished:
    clear_screen()
    print(hammer)
    name = input("Enter your name:\t")
    price = int(input("Enter price:\t"))
    bidding[name] = price
    temp = input("Are there any other bidders? yes or no:\t").lower()
    if (temp == "yes"):
        isFinished = False
    else:
        isFinished = True
highest = 0
highestBidder = ''
clear_screen()

for key, value in bidding.items():
    if value > highest:
        highestBidder = key
        highest = value
print(f"Highest bidder name is {highestBidder} and the price is {highest}")
