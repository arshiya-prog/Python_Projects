import requests
import os
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

config = {
    "query": input("Exercise description: ")
}

response = requests.post(url=nutrition_endpoint, json=config, headers=headers)
result = response.json()

# print(result["exercises"][0])

sheety_endpoint = os.environ.get("sheety")

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

data = {
    "workout": {
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}
sheety_response = requests.post(url=sheety_endpoint, json=data)
print(sheety_response.text)