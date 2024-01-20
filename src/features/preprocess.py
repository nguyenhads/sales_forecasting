import sys
from pathlib import Path
from typing import Dict, List, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sys.path.append('./')
from src.utils.data_manager import save_data
from src.utils.logger import init_logger
from src.utils.utils import load_config


def load_data(raw_data_dir: Path) -> pd.DataFrame:
    """Load sales data for 2016 and 2017."""
    df_sales2016 = pd.read_csv(raw_data_dir / '2016_sales.csv')
    df_sales2017 = pd.read_csv(raw_data_dir / '2017_sales.csv')
    return pd.concat([df_sales2016, df_sales2017], ignore_index=True)

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Check missing values in the DataFrame."""
    df_nan = pd.DataFrame({
        "counts": df.isna().sum(),
        "ratio (%)": np.round(df.isna().sum() / df.shape[0], 4) * 100,
    })
    return df_nan

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill NaN values in the 'sales' column with the mean of non-NaN values."""
    df_filled = df.copy()
    df_filled["sales"] = df_filled["sales"].fillna(df_filled["sales"].mean())
    return df_filled

def correct_outliers(df: pd.DataFrame, factor: int = 3) -> pd.DataFrame:
    """Identify and correct outliers in the 'sales' column by reducing them to the mean."""
    df_corrected = df.copy()

    # Identify outliers using z-score
    z_scores = (df_corrected["sales"] - df_corrected["sales"].mean()) / df_corrected["sales"].std()
    outlier_indices = np.abs(z_scores) > factor  # Adjust the threshold as needed
    # Correct outliers by reducing them to the mean
    df_corrected.loc[outlier_indices, "sales"] = df_corrected["sales"].mean()

    return df_corrected

def main():
    # Basic settings
    config = load_config('./config/path.yaml')
    LOG_DIR = Path(config["log"]["preprocess"])
    logger = init_logger(LOG_DIR)
    RAW_DATA_DIR = Path(config["path"]["raw_data"])
    OUTPUT_DIR = Path(config["path"]["preprocess_data"])

    # Load data
    df_sales = load_data(RAW_DATA_DIR)
    logger.info("Before filling missing values:")
    logger.info(check_missing_values(df_sales))

    # Fill missing values
    logger.info("After filling missing values:")
    df_sales_filled = fill_missing_values(df_sales)
    logger.info(check_missing_values(df_sales_filled))

    # Correct outliers
    logger.info("Corrected outlier!")
    df_sales_corrected = correct_outliers(df=df_sales_filled)

    # Save preprocessed data
    output_path = OUTPUT_DIR / 'sales_data_preprocessed.csv'
    save_data(df_sales_corrected, output_path)
    logger.info(f'Saved data to {output_path}')

if __name__ == "__main__":
    main()
