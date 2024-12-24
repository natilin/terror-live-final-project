import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_coordinates_by_location(city: str, country: str) -> dict:
    api_key = os.environ.get('OPENCAGE_API_KEY')
    try:
        response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}%2C+{country}&key={api_key}", verify=False).json()
        return response['results'][0]['geometry']
    except Exception:
        return {}


