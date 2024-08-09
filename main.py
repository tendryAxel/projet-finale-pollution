import dotenv
import sqlalchemy

import exctract_air_pollution
from utils import Database

psql_url = Database().create_url()
engine = sqlalchemy.create_engine(psql_url)

if __name__ == '__main__':
    dotenv.load_dotenv()
    exctract_air_pollution.main(engine)
