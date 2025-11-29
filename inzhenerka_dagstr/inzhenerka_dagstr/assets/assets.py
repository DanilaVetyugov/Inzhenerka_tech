from dagster import asset
from pandas import DataFrame, read_parquet
from datetime import datetime


@asset
def events() -> DataFrame:
    return read_parquet(path='s3://inzhenerka-public/scooters_data_generator/events.parguet')


@asset
def events_clean(events: DataFrame) -> DataFrame:
    df = events[['user_id', 'timestamp', 'type_id']].drop_duplicates()
    df['updated_at'] = datetime.now()
    return df
