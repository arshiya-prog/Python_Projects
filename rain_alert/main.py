import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat" : 18.520430,
    "lon" : 73.856743,
    "appid" : "4f6a41c787221da11589d8b2ac8d5cf2",
    "cnt" : 4,
}

data = requests.get(url=OWM_endpoint, params=parameters)
# print(data.status_code)
response = data.json()
print(response)
