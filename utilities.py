import pandas as pd
from sklearn import preprocessing


def normalize(series):
    min_max_scaler = preprocessing.MinMaxScaler()
    series = series.values.reshape(-1, 1)
    series_scaled = min_max_scaler.fit_transform(series)
    return series_scaled


def filterout(df, column, value):
    return df[df[column] != value]


def get_common_dates(df_list):
    common_dates = df_list[0].index
    for df in df_list[1:]:
        common_dates = common_dates.intersection(df.index)
    return common_dates