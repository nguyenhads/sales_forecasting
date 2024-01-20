import pandas as pd


def save_data(df: pd.DataFrame, path: str, type="csv"):
    """Save Pandas Dataframe

    Parameters
    ----------
    df : pd.DataFrame
        the data to be save
    path : str
        file path
    type : str, optional
        file format, by default "csv"

    Raises
    ------
    ValueError
        _description_
    """

    if type == "csv":
        df.to_csv(path, index=False)
    elif type == "feather":
        df.to_feather(path)
    else:
        raise ValueError(f"Unsupported file format: {type}")