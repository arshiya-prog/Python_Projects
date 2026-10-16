#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight, FlightData
from notification_manager import NotificationManager

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_data()

tomorrow = datetime.now().date() + timedelta(1)
six_months_from_today = datetime.now().date() + timedelta(180)

ORIGIN_CITY_IATA = "LHR"

flight_search = FlightSearch()

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA, 
        destination_city_code=destination["iataCode"], 
        from_time=tomorrow, 
        to_time=six_months_from_today
    )
    # pprint(flights)
    # pprint(sheet_data)

    cheapest_flight = find_cheapest_flight(data=flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(row_id=destination["id"], new_price=cheapest_flight.price)

        notification_manager = NotificationManager(
            price=cheapest_flight.price, 
            departure_iata=ORIGIN_CITY_IATA, 
            arrival_iata=destination["iataCode"], 
            outbound_date=tomorrow, 
            inbound_date=six_months_from_today
        )
        notification_manager.send_mail()