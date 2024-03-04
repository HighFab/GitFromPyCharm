import pandas as pd


def raw_data():
    df = pd.read_csv('data/produkt_klima_tag_19470101_20221231_05490.txt', sep=";")
    df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d')
    df['Year'] = df['MESS_DATUM'].dt.year
    df.columns = map(str.strip, df.columns)  # Remove whitespace from headers.
    return df


def import_data():
    df = raw_data()
    df = df[['MESS_DATUM', 'Year', 'TMK']]
    print(df)
    return df


def import_slicer():
    df = raw_data()
    df_year = df['Year'].unique()
    print(df_year)
    return df_year
