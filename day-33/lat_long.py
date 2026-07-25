import requests
from datetime import datetime

# MY_LAT = 18.5509
# MY_LONG = 73.9349
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
TIME_NOW = datetime.now()

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

# response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(TIME_NOW)