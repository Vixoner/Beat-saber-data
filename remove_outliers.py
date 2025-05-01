import pandas as pd

def remove_outliers(data_df: pd.DataFrame, threshold=3) -> pd.DataFrame:
    df_cleaned = data_df.copy()

    for column in df_cleaned.columns:
        if column != 'rank':
            mean = df_cleaned[column].mean()
            std = df_cleaned[column].std()
            df_cleaned = df_cleaned[(df_cleaned[column] > mean - threshold * std) & (df_cleaned[column] < mean + threshold * std)]
    return df_cleaned