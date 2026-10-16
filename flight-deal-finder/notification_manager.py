import smtplib
import os
from dotenv import load_dotenv

class NotificationManager:
    load_dotenv()

    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, departure_iata, arrival_iata, outbound_date, inbound_date):
        self.price = price
        self.source = departure_iata
        self.destination = arrival_iata
        self.outbound = outbound_date
        self.inbound = inbound_date

    def send_mail(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        message = (
            f"Subject: Low price alert!\n\n"
            f"Only GBP {self.price} to fly from {self.source} to {self.destination}, "
            f"from {self.outbound} until {self.inbound}."
        )
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=message.encode("utf-8"),
            )