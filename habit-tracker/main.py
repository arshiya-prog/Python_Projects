import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN 
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kms did you cycle today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260919"

update_pixel_config = {
    "quantity": "7.8"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260919"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)