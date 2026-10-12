#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight, FlightData

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

flight_search = FlightSearch()
flights = flight_search.check_flights(
    origin_city_code="LHR", 
    destination_city_code="CDG", 
    from_time=tomorrow, 
    to_time=six_months_from_today
)
# pprint(flights)
# pprint(sheet_data)

cheapest_flight = find_cheapest_flight(data=flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
    pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
    data_manager.update_lowest_price(row_id=sheet_data[0]["id"], new_price=cheapest_flight.price)