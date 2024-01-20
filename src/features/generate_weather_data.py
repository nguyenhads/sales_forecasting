import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append("./")
from src.utils.data_manager import save_data
from src.utils.logger import init_logger
from src.utils.utils import load_config

# Basic settings
config = load_config('./config/path.yaml')
LOG_DIR = Path(config["log"]["weather_data"])
logger = init_logger(LOG_DIR)
OUTPUT_DIR = Path(config["path"]["preprocess_data"])


def generate_seasonal_weather(month: int) -> tuple:
    """Generate seasonal weather data for a given month."""
    mean_temp_lst = [15, 25, 15, 5]
    std_temp = 5
    mean_humidity_lst = [50, 80, 60, 30]
    std_humidity = 10

    if 3 <= month <= 5:
        season = "spring"
        temperature = max(0, np.random.normal(mean_temp_lst[0], std_temp))
        humidity = max(0, np.random.normal(mean_humidity_lst[0], std_humidity))
    elif 6 <= month <= 8:
        season = "summer"
        temperature = max(0, np.random.normal(mean_temp_lst[1], std_temp))
        humidity = max(0, np.random.normal(mean_humidity_lst[1], std_humidity))
    elif 9 <= month <= 11:
        season = "fall"
        temperature = max(0, np.random.normal(mean_temp_lst[2], std_temp))
        humidity = max(0, np.random.normal(mean_humidity_lst[2], std_humidity))
    else:
        season = "winter"
        temperature = max(0, np.random.normal(mean_temp_lst[3], std_temp))
        humidity = max(0, np.random.normal(mean_humidity_lst[3], std_humidity))

    return temperature, humidity, season


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

    weather_data = []

    for date in date_range:
        month = date.month
        temperature, humidity, season = generate_seasonal_weather(month)

        weather_data.append(
            {
                "date": date,
                "temperature": temperature,
                "humidity": humidity,
                "season": season
            }
        )

    return pd.DataFrame(weather_data)


def main():
    start_date = "2016-01-01"
    end_date = "2017-12-31"

    logger.info(f"Start generate weather data from {start_date} - {end_date}!")
    df_weather = generate_weather_data(start_date=start_date, end_date=end_date)
    output_path = OUTPUT_DIR / 'weather.csv'
    save_data(df=df_weather, path=output_path)
    logger.info(f"Save weather data to {output_path}")


if __name__ == "__main__":
    main()
