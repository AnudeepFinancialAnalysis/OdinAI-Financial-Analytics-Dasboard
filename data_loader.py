import pandas as pd

def load_data(path='Growjo_Enriched_Dataset.csv'):
    df = pd.read_csv(path)
    return df
