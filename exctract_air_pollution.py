import sqlalchemy
import datetime
import os
import dotenv

from utils import find_city_position, get_pollution


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
    psql_url = f'postgresql+psycopg2://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@localhost/{os.getenv("DB_NAME")}'
    engine = sqlalchemy.create_engine(psql_url)
    return pollution.to_sql('weather', con=engine, if_exists='append', index=False)


def main(): save_hourly_weather_to_csv("Paris")


if __name__ == '__main__':
    dotenv.load_dotenv()
    main()
