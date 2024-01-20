import os
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append("./")
from src.utils.data_manager import save_data


def generate_weather_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Generate Tokyo Weather Data

    Parameters
    ----------
    start_date : str
        Start date of data
    end_date : str
        End date of data

    Returns
    -------
    pd.DataFrame
        Weather Data Frame
    """

    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    date_range = pd.date_range(start_date, end_date, freq="D")
    # print(date_range)

    weather_data = []
    mean_temp_lst = [15, 25, 15, 5]
    std_temp = 5
    mean_hudmidity_lst = [50, 80, 60, 30]
    std_humidity = 10

    for date in date_range:
        month = date.month
        is_spring = (3 <= month <= 5)
        is_summer = (6 <= month <= 8)
        is_fall = (9 <= month <= 11)

        if is_spring:
            season = "spring"
            temperature = max(0, np.random.normal(mean_temp_lst[0], std_temp))
            humidity = max(0, np.random.normal(mean_hudmidity_lst[0], std_humidity))
        elif is_summer:
            season = "summer"
            temperature = max(0, np.random.normal(mean_temp_lst[1], std_temp))
            humidity = max(0, np.random.normal(mean_hudmidity_lst[1], std_humidity))
        elif is_fall:
            season = "fall"
            temperature = max(0, np.random.normal(mean_temp_lst[2], std_temp))
            humidity = max(0, np.random.normal(mean_hudmidity_lst[2], std_humidity))
        else:
            season = "winter"
            temperature = max(0, np.random.normal(mean_temp_lst[3], std_temp))
            humidity = max(0, np.random.normal(mean_hudmidity_lst[3], std_humidity))

        weather_data.append(
            {
                "date": date,
                "temperature": temperature,
                "hudmity": humidity,
                "season": season
            }
        )

    return pd.DataFrame(weather_data)


def main():
    start_date = "2016-01-01"
    end_date = "2017-12-31"

    df_weather = generate_weather_data(start_date=start_date, end_date=end_date)
    
    output_path = Path("./data/preprocessed-data/weather.csv")
    save_data(df=df_weather, path=output_path)


main()
