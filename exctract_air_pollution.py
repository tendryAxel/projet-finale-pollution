import pandas as pd
import sqlalchemy
import datetime

from utils import find_city_position, get_pollution, Database

psql_url = Database().create_url()
engine = sqlalchemy.create_engine(psql_url)


def save_hourly_weather_to_csv(city: str, date: datetime.datetime = datetime.datetime.today()) -> None:
    location = find_city_position(city)
    pollution = get_pollution(location, date)
    pollution["city_name"] = city
    return pollution.to_sql('weather', con=engine, if_exists='append', index=False)


def save_hourly_weather_of_many_to_csv(cities: list[str], date: datetime.datetime = datetime.datetime.today()) -> None:
    city_dataframe = pd.DataFrame({
        "name": cities
    })
    for city in cities:
        save_hourly_weather_to_csv(city, date)
    city_dataframe.to_sql("city", con=engine, if_exists='replace', index=False)


def main(): save_hourly_weather_of_many_to_csv(["Paris", "London"])
