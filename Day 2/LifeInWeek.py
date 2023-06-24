# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

new_Age = int(age)

remaining_year = 90 - new_Age
remaining_days = remaining_year * 365
remaining_week = remaining_year * 52
remaining_month = remaining_year * 12

print(
    f"You have {remaining_days} days, {remaining_week} weeks, and {remaining_month} months left.")
