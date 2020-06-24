import ctypes
import datetime
import os
import time
from datetime import date

import requests

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

API_KEY = os.getenv("WAPI_KEY")
# Derby
CITY_ID = os.getenv("CITY_ID")  # 2651347
# bangalore
#CITY_ID = 1277333


def set_wallpaper(wallpaper_path=None):
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0
    )


def get_wallpaper_key(*, hour, weather, hours):

    if date.today().weekday() == 6:
        return "Sunday"
    if weather == "Clear":
        return "Day" if hour in hours else "Night"
    if weather == "Clouds":
        return "Clouds"
    if weather == "Drizzle":
        return "Drizzle"
    if weather == "Rain":
        return "Rain"
    if weather == "Thunderstorm":
        return "Storm"
    return "Other"


API_URL = "http://api.openweathermap.org/data/2.5/weather"
PAYLOAD = {"appid": API_KEY, "id": CITY_ID}

# required hex code for SPI_SETDESKWALLPAPER
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow
SPI_SETDESKWALLPAPER = 0x0014
# r"C:\Users\singhs\Desktop\weather"
WALLPAPERS_DIR = os.path.join(ROOT_DIR, "asset")
WEATHER_REFRESH_RATE = 600


def main():
    weather_wallpaper_filename_dict = {
		"Clouds": "clouds.jpg",
		"Day": "day.jpg",
		"Drizzle": "drizzle.jpg",
		"Night": "moon.jpg",
		"Other": "other.jpg",
		"Rain": "rain.jpg",
		"Storm": "storm.jpg",
		"Sunday": "sunday.jpg"
    }
    while True:
        current_hour = datetime.datetime.now().hour
        json_data = requests.get(API_URL, params=PAYLOAD).json()
        daytime_hours = range(6, 18)
        current_weather = json_data["weather"][0]["main"]
        wallpaper_key = get_wallpaper_key(
            hour=current_hour, weather=current_weather, hours=daytime_hours,
        )
        wallpaper_path = os.path.join(
            WALLPAPERS_DIR, weather_wallpaper_filename_dict[wallpaper_key]
        )
        set_wallpaper(wallpaper_path)
        time.sleep(WEATHER_REFRESH_RATE)

if __name__ == "__main__":
    main()
