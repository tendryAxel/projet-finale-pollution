import dotenv
import sqlalchemy

import exctract_air_pollution
import transform_calc_aqi
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

    # Calculate the AQI of the stored data
    # pollution store the AQI based on the POLLUTANT_PM10
    transform_calc_aqi.main(engine)
