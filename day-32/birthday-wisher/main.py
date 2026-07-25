import datetime as dt
import random
import smtplib
import pandas as pd
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
LETTERS_TEMPLATES = ["day-32/birthday-wisher/letter_templates/letter_1.txt", 
                "day-32/birthday-wisher/letter_templates/letter_2.txt",
                "day-32/birthday-wisher/letter_templates/letter_3.txt"
                ]

selected_template = random.choice(LETTERS_TEMPLATES)

with open(selected_template) as file:
    text = file.read()

now = dt.datetime.now()
current_day = now.day
current_month = now.month

birthday_df = pd.read_csv("day-32/birthday-wisher/birthdays.csv")
birthday_dict = birthday_df.to_dict()

for key in birthday_dict["name"]:       # Keys inside nested dict (0, 1)
    if birthday_dict["day"][key] == current_day and birthday_dict["month"][key] == current_month:
        name = birthday_dict["name"][key]
        email = birthday_dict["email"][key]
                        
        personalised_text = text.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=email, 
                msg=f"Subject: Happy Birthday!\n\n{personalised_text}"
            )