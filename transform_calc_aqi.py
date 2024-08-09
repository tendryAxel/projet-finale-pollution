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


def main(engine: Engine):
    all_pollution = pd.read_sql_table("weather_lake", con=engine.connect())
    all_pollution["aqi"] = all_pollution.apply(calc_aqi, axis=1)
    all_pollution.to_sql("weather", con=engine, if_exists="replace")
