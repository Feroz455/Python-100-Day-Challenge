print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 20, or 15? "))
ppl = int(input("How many people to split the bill? "))
PersonBill = bill / ppl
personTip = PersonBill * (tip / 100)


print(round(PersonBill+personTip, 2))
