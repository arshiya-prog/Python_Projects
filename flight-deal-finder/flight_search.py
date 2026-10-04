from dotenv import load_dotenv
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    load_dotenv()

    def __init__(self) -> None:
        self._api_key = os.getenv("SERP_API_KEY")
        