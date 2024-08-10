import datetime
import os.path

import pandas as pd

from .utils import find_city_position, get_pollution_in_range


def save_hourly_pollution_to_csv_in_range(
        engine,
        city: str,
        start: datetime.datetime,
        end: datetime.datetime = datetime.datetime.today()) -> None:
    location = find_city_position(city)
    pollution = get_pollution_in_range(location, start, end)
    pollution["dt"] = pd.to_datetime(pollution["dt"], errors='coerce')
    pollution["city_name"] = city
    return pollution.to_sql('pollution_lake', con=engine, if_exists='append', index=False)


def save_hourly_pollution_of_many_to_csv_in_range(
        engine,
        cities: list[str],
        start: datetime.datetime,
        end: datetime.datetime = datetime.datetime.today()) -> None:
    city_dataframe = pd.DataFrame({
        "name": cities
    })
    for city in cities:
        save_hourly_pollution_to_csv_in_range(engine, city, start, end)
    city_dataframe.to_sql("city_lake", con=engine, if_exists='replace', index=False)


def main_with_date_range(engine, start: datetime.datetime, end: datetime.datetime = datetime.datetime.today()) -> None:
    save_hourly_pollution_of_many_to_csv_in_range(
        engine,
        list(pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "Geographic_Data.csv"))["Location"]),
        start,
        end
    )


def save_hourly_pollution_to_csv(engine, city: str, date: datetime.datetime = datetime.datetime.today()) -> None:
    return save_hourly_pollution_to_csv_in_range(engine, city, date - datetime.timedelta(days=1), date)


def save_hourly_pollution_of_many_to_csv(engine, cities: list[str], date: datetime.datetime = datetime.datetime.today()) -> None:
    return save_hourly_pollution_of_many_to_csv_in_range(engine, cities, date - datetime.timedelta(days=1), date)


def main(engine):
    main_with_date_range(engine, datetime.datetime.today() - datetime.timedelta(days=1), datetime.datetime.today())
