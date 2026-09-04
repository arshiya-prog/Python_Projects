import requests
from twilio.rest import Client
import os

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat" : 18.520430,
    "lon" : 73.856743,
    "appid" : os.environ["OWM_API_KEY"],
    "cnt" : 4,
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️.",
        from_=f"whatsapp:{os.environ["TWILIO_FROM_NUMBER"]}",
        to=f"whatsapp:{os.environ["MY_PHONE_NUMBER"]}",
    )
    print(message.status)