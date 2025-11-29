from dagster import asset
from pandas import DataFrame, read_parquet
from datetime import datetime


@asset
def events() -> DataFrame:
    df = read_parquet(path='s3://inzhenerka-public/scooters_data_generator/events.parguet')
    clean_df = df[['user_id', 'timestamp', 'type_id']].drop_duplicates()
    clean_df['updated_at'] = datetime.now()
    return clean_df
