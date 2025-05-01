import pandas as pd 

def generate_attribute_stats(data_df: pd.DataFrame):
    print("Wartości minimalne:")
    print(data_df.min())

    print("Wartości maksymalne:")
    print(data_df.max())

    print("Wartości średnie:")
    print(data_df.mean())