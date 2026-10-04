import requests
import os
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data(self):
        load_dotenv()
        self.sheety_url = os.getenv("SHEETY_URL")
        self.headers = {
            "Authorization":os.getenv("SHEETY_AUTH")
        }

        self.data = requests.get(url=self.sheety_url, headers=self.headers)
        return self.data.json()["sheet1"]