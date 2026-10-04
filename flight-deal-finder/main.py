#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta

requests_cache.install_cache(cache_name="flight_cache")

data_manager = DataManager()
sheet_data = data_manager.get_data()

tomorrow = datetime.now().date() + timedelta(1)
six_months_from_today = datetime.now().date() + timedelta(180)

pprint(sheet_data)