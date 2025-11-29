from dagster import Definitions, load_assets_from_modules
from inzhenerka_dagstr import assets

all_assets = load_assets_from_modules([assets])

definitions = Definitions(
    assets=all_assets
)


