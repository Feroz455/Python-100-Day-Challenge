import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)


def sendMail(subject, message):
    password = "ljsxfazyrggswmpi"
    my_email = "sayyidmohammadfirozmahmud@gmail.com"
    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="sayyidmohammadfirozmahmud@hotmail.com", 
                            msg=f"Subject:{subject}\n\n{message}")
        connection.close()

if weekday == 3:
   with open("./SMTP/quotes.txt") as Quotes:
    data = [line.strip() for line in Quotes.readlines()]
   
    sendMail("From bottom of my heart", random.choice(data))

