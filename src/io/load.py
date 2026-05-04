import pandas as pd
from pathlib import Path
import logging

def load_data():

    logger = logging.getLogger(__name__)
    logger.info("Loading data")

    root_dir = Path.cwd()
    data_path = root_dir / "data/raw"

    street_list = []
    outcomes_list = []
    search_list = []

    for folder in data_path.iterdir():
        if folder.is_dir():
            street_file = folder / f"{folder.name}-north-yorkshire-street.csv"
            outcomes_file = folder / f"{folder.name}-north-yorkshire-outcomes.csv"
            search_file = folder / f"{folder.name}-north-yorkshire-stop-and-search.csv"

            if street_file.exists():
                df = pd.read_csv(street_file)
                df["source_month"] = folder.name
                street_list.append(df)

            if outcomes_file.exists():
                df = pd.read_csv(outcomes_file)
                df["source_month"] = folder.name
                outcomes_list.append(df)

            if search_file.exists():
                df = pd.read_csv(search_file)
                df["source_month"] = folder.name
                search_list.append(df)

    street = pd.concat(street_list, ignore_index = True)
    logger.info("Loaded street")
    outcomes = pd.concat(outcomes_list, ignore_index = True)
    logger.info("Loaded outcomes")
    search = pd.concat(search_list, ignore_index = True)
    logger.info("Loaded search")

    logger.info("Loading complete")

    return street, outcomes, search