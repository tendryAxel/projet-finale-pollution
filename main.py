import datetime
import os

import dotenv
import sqlalchemy

from weather import transform, exctract_air_pollution
from weather.utils import Database, conditional_action_by_list_env

if __name__ == '__main__':
    # Load .env
    dotenv.load_dotenv()

    # Create database(postgresql) connection
    psql_url = Database().create_url()
    engine = sqlalchemy.create_engine(psql_url)

    # Store air pollution in database with the following pattern
    # pollution_lake and city_lake as DataLake to store the fetched data
    range_start, range_end = os.getenv("RANGE_START"), os.getenv("RANGE_END")
    try:
        date_format = "%Y-%m-%d"
        range_start_d = datetime.datetime.strptime(range_start, date_format)
        range_end_d = datetime.datetime.strptime(range_end, date_format)
        conditional_action_by_list_env(
            [range_start, range_end],
            lambda: exctract_air_pollution.main_with_date_range(engine, range_start_d, range_end_d),
            lambda: exctract_air_pollution.main(engine)
        )
    except:
        exctract_air_pollution.main(engine)

    """
        - Calculate the AQI and store in pollution
        - Store geographic and demographic data in the database
    """
    transform.main(engine)
