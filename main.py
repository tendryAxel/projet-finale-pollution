import dotenv
import sqlalchemy

import exctract_air_pollution
import transform_calc_aqi
from utils import Database

if __name__ == '__main__':
    dotenv.load_dotenv()

    psql_url = Database().create_url()
    engine = sqlalchemy.create_engine(psql_url)

    exctract_air_pollution.main(engine)
    transform_calc_aqi.main(engine)
