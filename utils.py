import datetime
import math
import os
import pandas as pd

from airpyllution.airpyllution import get_pollution_history
import geopy

geolocator = geopy.Nominatim(user_agent="devoir-données2-geodecoder")


def convert_datetime_to_unix_timestamp(dt: datetime.datetime) -> int: return math.floor((dt - datetime.datetime(
    1970, 1, 1)).total_seconds())


def find_city_position(city: str) -> geopy.Location: return geolocator.geocode(city)


def get_pollution(location: geopy.Location, date: datetime.datetime) -> pd.DataFrame:
    return get_pollution_history(
        convert_datetime_to_unix_timestamp(date - datetime.timedelta(days=1)),
        convert_datetime_to_unix_timestamp(date),
        location.latitude,
        location.longitude,
        os.getenv("OPEN_WEATHER_API_KEY")
    )
