from dotenv import load_dotenv
import os
import requests
# import serpapi

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    load_dotenv()

    def __init__(self) -> None:
        self._api_key = os.getenv("SERP_API_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # client = serpapi.Client(api_key=self._api_key)
        # results = client.search({
        #     "engine": "google_flights",
        #     "departure_id": origin_city_code,
        #     "arrival_id": destination_city_code,
        #     "currency": "INR",
        #     "type": "2",
        #     "outbound_date": from_time
        # })

        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        results = requests.get(url=os.getenv("SERP_URL"), params=query)

        return results.json()