import pandas as pd
import sqlalchemy
import datetime
import dotenv

from utils import find_city_position, get_pollution, Database

psql_url = Database().create_url()
engine = sqlalchemy.create_engine(psql_url)


def save_hourly_weather_to_csv(city: str, date: datetime.datetime = datetime.datetime.today()) -> None:
    """
    Le resultat de cette operation est:
        - Soit une erreur de None parce qu'il n'y a pas de données de pollution le jour choisi
        - Soit le l'historique sera sauvegadrer dans un fichier .csv

    :param city: Un nom qui permetterai de chercher la ville en question
    :param date:
    :return: Normalement rien
    """
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


if __name__ == '__main__':
    dotenv.load_dotenv()
    main()
