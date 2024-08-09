import dotenv
import sqlalchemy

import exctract_air_pollution
import transform
from utils import Database

if __name__ == '__main__':
    # Load .env
    dotenv.load_dotenv()

    # Create database(postgresql) connection
    psql_url = Database().create_url()
    engine = sqlalchemy.create_engine(psql_url)

    # Store air pollution in database with the following pattern
    # pollution_lake and city_lake as DataLake to store the fetched data
    exctract_air_pollution.main(engine)

    """
        - Calculate the AQI and store in pollution
        - Store geographic and demographic data in the database
    """
    transform.main(engine)
