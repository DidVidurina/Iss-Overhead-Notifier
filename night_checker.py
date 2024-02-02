import requests
from datetime import datetime as datetime

MY_LAT = 51.700329
MY_LONG = 0.108655
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted": 0,
}
API_RESPONSE = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS)
API_RESPONSE.raise_for_status()


class NightChecker():
    def __init__(self):
        super().__init__()
        self.night = False
        self.sunrise = (str(API_RESPONSE.json()["results"]["sunrise"])).split("T")[1].split("+")[0]
        self.sunset = (str(API_RESPONSE.json()["results"]["sunset"])).split("T")[1].split("+")[0]
        self.actual_time_now = str(datetime.now().time()).split(".")[0]
        self.sunrise_long = int(self.sunrise.replace(":",""))
        self.sunset_long = int(self.sunset.replace(":",""))
        self.actual_time_now_long = int(self.actual_time_now.replace(":",""))

    def checker_return(self):
        if self.actual_time_now_long > self.sunset_long:
            self.night = True
        elif self.actual_time_now_long < self.sunrise_long:
            self.night = True
        else:
            self.night = False
