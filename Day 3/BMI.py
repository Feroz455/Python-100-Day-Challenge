# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int(weight) / (float(height) ** 2)
print(int(BMI))

if BMI < 18.5:
    print(f"Your bmi is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your bmi is {BMI}, you are normal weight")
elif BMI < 30:
    print(f"Your bmi is {BMI}, you are overweight")
elif BMI < 35:
    print(f"Your bmi is {BMI}, you are obese")
else:
    print(f"Your bmi is {BMI}, you are clinically obese")
