import requests
import os

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

print(result["exercises"][0])

# sheety_endpoint = "https://api.sheety.co/73c1cf4cc802480f28f89d707bee95ac/myWorkouts/workouts"

# data = {
#     "workout": result["exercises"][0]
# }
# sheety_response = requests.post(url=sheety_endpoint, json=data)
# print(sheety_response.text)