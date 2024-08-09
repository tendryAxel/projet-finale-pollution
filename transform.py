import os

import aqi
import pandas as pd
from sqlalchemy import Engine


def calc_aqi(line: pd.Series):
    return aqi.to_iaqi(aqi.POLLUTANT_PM10, f'{line["pm10"]}')
    # return aqi.to_aqi([
    #     (aqi.POLLUTANT_CO_8H, f'{line["co"]}'),
    #     (aqi.POLLUTANT_NO2_1H, f'{line["no2"]}'),
    #     (aqi.POLLUTANT_O3_1H, f'{line["o3"]}'),
    #     (aqi.POLLUTANT_O3_8H, f'{line["o3"]}'),
    #     (aqi.POLLUTANT_SO2_1H, f'{line["so2"]}'),
    #     (aqi.POLLUTANT_PM10, f'{line["pm10"]}'),
    # ])


def create_geographic(engine: Engine, file_path: str):
    pd.read_csv(file_path, index_col=0).to_sql("geographic", con=engine, if_exists='replace')


def create_demographic(engine: Engine, file_path: str):
    pd.read_csv(file_path, index_col=0).to_sql("demographic", con=engine, if_exists='replace')


def create_pollution(engine: Engine):
    all_pollution = pd.read_sql_table("pollution_lake", con=engine.connect())
    all_pollution["aqi"] = all_pollution.apply(calc_aqi, axis=1)
    all_pollution.to_sql("pollution", con=engine, if_exists="replace")


def main(engine: Engine):
    create_pollution(engine)
    create_demographic(engine, os.path.join(os.path.dirname(__file__), "data", "Demographic_Data.csv"))
    create_geographic(engine, os.path.join(os.path.dirname(__file__), "data", "Geographic_Data.csv"))
