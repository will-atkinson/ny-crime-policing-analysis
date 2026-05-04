import pandas as pd
import logging

def clean_street(df: pd.DataFrame) -> pd.DataFrame:

    logger = logging.getLogger(__name__)
    logger.info("Cleaning street")

    df = df.copy()

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df["month"] = pd.to_datetime(df["month"], errors = "coerce")

    df["crime_type"] = df["crime_type"].astype("string").str.strip()
    df["last_outcome_category"] = df["last_outcome_category"].astype("string").str.strip()

    df["has_crime_id"] = df["crime_id"].notna()
    df["is_asb"] = df["crime_type"] == "Anti-social behaviour"
    df["has_location"] = df["latitude"].notna() & df["longitude"].notna()

    df = df.drop(columns = ["context"], errors = "ignore")

    before_dedupe = len(df)
    logger.info(f"street rows before dedupe: {before_dedupe}")

    with_id = df.loc[df["has_crime_id"]].copy()
    without_id = df.loc[~df["has_crime_id"]].copy()

    logger.info(f"street rows with crime_id: {len(with_id)}")
    logger.info(f"street rows without crime_id: {len(without_id)}")

    with_id = with_id.drop_duplicates(subset = ["crime_id"], keep = "first")  # type: ignore
    df = pd.concat([with_id, without_id], ignore_index = True) # type: ignore

    after_dedupe = len(df)
    rows_dropped = before_dedupe - after_dedupe

    logger.info(f"street rows after dedupe: {after_dedupe}")
    logger.info(f"street rows dropped: {rows_dropped}")

    logger.info(f"Cleaning complete street rows: {len(df)}")

    return df
