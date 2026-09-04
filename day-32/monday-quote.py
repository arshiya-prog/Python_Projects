import datetime as dt
import smtplib
import random
import os

my_email = os.environ.get("MY_EMAIL")      # Add the mail ID
password = os.environ.get("MY_PASSWORD")           # Add your password
date = dt.datetime.now()

day_of_week = date.weekday()

if day_of_week == 2:
    with open("day-32/quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("ADD THE SMTP SERVER") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="RECEPIENT's MAIL ID", 
            msg=f"Subject: Quote of the Day\n\n{quote}"
        )