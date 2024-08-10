import datetime
import math
import os
from typing import Callable

import pandas as pd

from airpyllution.airpyllution import get_pollution_history
import geopy

geolocator = geopy.Nominatim(user_agent="devoir-données2-geodecoder")


def convert_datetime_to_unix_timestamp(dt: datetime.datetime) -> int: return math.floor((dt - datetime.datetime(
    1970, 1, 1)).total_seconds())


def find_city_position(city: str) -> geopy.Location: return geolocator.geocode(city)


def get_pollution(location: geopy.Location, date: datetime.datetime) -> pd.DataFrame:
    return get_pollution_in_range(location, date - datetime.timedelta(days=1), date)


def get_pollution_in_range(location: geopy.Location, start: datetime.datetime, end: datetime.datetime) -> pd.DataFrame:
    return get_pollution_history(
        convert_datetime_to_unix_timestamp(start),
        convert_datetime_to_unix_timestamp(end),
        location.latitude,
        location.longitude,
        os.getenv("OPEN_WEATHER_API_KEY")
    )


def conditional_action_by_list_env(envs: list[str | None], success_action: Callable, defeat_action: Callable) -> None:
    if len([env for env in envs if env is None]) == 0:
        print("Successfully load all environments for this condition")
        success_action()
    else:
        defeat_action()


class Database:
    DB_PASSWRD_ENV_NAME = "DB_PASSWORD"

    def __init__(self):
        self.username = os.getenv("DB_USERNAME")
        self.database_name = os.getenv("DB_NAME")
        self.password = os.getenv(self.DB_PASSWRD_ENV_NAME)
        self.host = os.getenv("DB_HOST")

        self.username = self.username if self.username else "postgres"
        self.database_name = self.database_name if self.database_name else "pollution"
        self.host = self.host if self.host else "localhost"

        if self.password is None:
            raise RuntimeError(f"Database password is not provided \n\tSet {self.DB_PASSWRD_ENV_NAME} env")

    def create_url(self) -> str:
        return f'postgresql+psycopg2://{self.username}:{self.password}@{self.host}/{self.database_name}'
