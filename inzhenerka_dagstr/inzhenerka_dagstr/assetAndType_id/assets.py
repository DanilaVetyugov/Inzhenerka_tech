
from dagster import asset, InMemoryIOManager, AssetKey
from pandas import DataFrame, read_parquet
from datetime import datetime


@asset
def events() -> DataFrame:
    return read_parquet(path='s3://inzhenerka-public/scooters_data_generator/events.parguet')

@asset(
    io_manager_def=InMemoryIOManager(),
    deps=[AssetKey('events')]

)
def event_types() -> DataFrame:
    return DataFrame({'type_id': [0,1,2,3], 'type': ['start_search', 'book_scooter','release_scooter', 'cancel_search']})

@asset
def events_clean(events: DataFrame) -> DataFrame:
    df = events[['user_id', 'timestamp', 'type_id']].drop_duplicates()
    df['updated_at'] = datetime.now()
    return df

