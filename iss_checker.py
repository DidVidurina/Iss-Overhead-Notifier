import time

import requests
"""Update these constants with your location coordinates"""
MY_LONG = 0.108655
MY_LAT = -51.700329

iss_data = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data.raise_for_status()

class IssChecker:
    def __init__(self):
        super().__init__()
        self.close = False
        self.long_close = False
        self.lat_close = False
        self.higher_long = 0
        self.lower_long = 0
        self.higher_lat = 0
        self.lower_lat = 0
        self.iss_longitude = float(iss_data.json()["iss_position"]["longitude"])
        self.iss_latitude = float(iss_data.json()["iss_position"]["latitude"])
        self.iss_long_tuple = (self.iss_longitude - 5.1, self.iss_longitude + 5.1)
        self.iss_lat_tuple = (self.iss_latitude - 5.1, self.iss_latitude + 5.1)

    def fetch_data(self):
        iss_data = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_data.raise_for_status()
        self.iss_longitude = float(iss_data.json()["iss_position"]["longitude"])
        self.iss_latitude = float(iss_data.json()["iss_position"]["latitude"])
        self.iss_longitude = float(iss_data.json()["iss_position"]["longitude"])
        self.iss_latitude = float(iss_data.json()["iss_position"]["latitude"])
        self.iss_long_tuple = (self.iss_longitude - 5.1, self.iss_longitude + 5.1)
        self.iss_lat_tuple = (self.iss_latitude - 5.1, self.iss_latitude + 5.1)

    def check_proximity(self):
        if self.iss_long_tuple[0] <= MY_LONG and  self.iss_long_tuple[1] >= MY_LONG:
            self.long_close = True
        else:
            self.long_close = False
        if self.iss_lat_tuple[0] <= MY_LAT and self.iss_lat_tuple[1] >= MY_LAT:
            self.lat_close = True
        else:
            self.lat_close = False

        if self.long_close is True and self.lat_close is True:
            self.close = True
        else:
            self.close = False











