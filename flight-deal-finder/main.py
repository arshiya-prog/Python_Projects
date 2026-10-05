#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

requests_cache.install_cache(cache_name="flight_cache")

data_manager = DataManager()
sheet_data = data_manager.get_data()

tomorrow = datetime.now().date() + timedelta(1)
six_months_from_today = datetime.now().date() + timedelta(180)

flight_search = FlightSearch()

flight = flight_search.check_flights(origin_city_code="LHR", destination_city_code="CDG", from_time=tomorrow, to_time=six_months_from_today)
pprint(flight)
# pprint(sheet_data)