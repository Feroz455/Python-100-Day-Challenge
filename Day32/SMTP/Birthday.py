#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explanations


from datetime import datetime
import pandas
import random
import smtplib


from datetime import datetime
import pandas as pd
import random
import smtplib
import os

# Email credentials
MY_EMAIL = "sayyidmohammadfirozmahmud@gmail.com"
MY_PASSWORD = "ljsxfazyrggswmpi"

# Get today's date
today = datetime.now()
today_month = today.month
today_day = today.day

# Load birthday data from CSV
data = pd.read_csv("./SMTP/birthdays.csv")

# Filter birthdays that match today's date
today_birthdays = data[(data["month"] == today_month) & (data["day"] == today_day)]

# Check if there are any birthdays today
if not today_birthdays.empty:
    # Choose a random letter template
    letter_template = f"./SMTP/letter_templates/letter_{random.randint(1, 3)}.txt"

    # Read the selected letter template
    with open(letter_template, "r") as file:
        letter_content = file.read()

    # Loop through each birthday person
    for index, row in today_birthdays.iterrows():
        # Customize the letter content with the person's name
        customized_letter = letter_content.replace("[NAME]", row["name"])

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure the connection
            connection.starttls()

            # Log in to your email account
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            # Send the birthday email
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject: Happy Birthday!\n\n{customized_letter}"
            )

print("Birthday emails sent successfully!")
