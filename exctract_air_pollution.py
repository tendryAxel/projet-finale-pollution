import pandas as pd
import datetime

from sqlalchemy import Engine

from utils import find_city_position, get_pollution, Database


def save_hourly_pollution_to_csv(engine: Engine, city: str, date: datetime.datetime = datetime.datetime.today()) -> None:
    location = find_city_position(city)
    pollution = get_pollution(location, date)
    pollution["city_name"] = city
    pollution["aqi"] = 0
    return pollution.to_sql('pollution_lake', con=engine, if_exists='append', index=False)


def save_hourly_pollution_of_many_to_csv(engine: Engine, cities: list[str], date: datetime.datetime = datetime.datetime.today()) -> None:
    city_dataframe = pd.DataFrame({
        "name": cities
    })
    for city in cities:
        save_hourly_pollution_to_csv(engine, city, date)
    city_dataframe.to_sql("city_lake", con=engine, if_exists='replace', index=False)


def main(engine: Engine): save_hourly_pollution_of_many_to_csv(engine, ["Paris", "London"])
