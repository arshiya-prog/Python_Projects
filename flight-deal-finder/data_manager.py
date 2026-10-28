import requests
import os
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._auth = os.getenv("SHEETY_AUTH")

    def get_data(self):
        load_dotenv()
        self.sheety_url = os.getenv("SHEETY_URL")
        self.headers = {
            "Authorization":self._auth
        }

        self.data = requests.get(url=self.sheety_url, headers=self.headers)
        return self.data.json()["sheet1"]

    def update_lowest_price(self, row_id, new_price):
        updated_data = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }
        self.url = f"{self.sheety_url}/{row_id}"
        requests.put(url=self.url, json=updated_data, headers=self.headers)

    def get_customer_emails(self):
        # self.response = reques