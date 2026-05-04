import pandas as pd
import logging

def clean_outcomes(df: pd.DataFrame) -> pd.DataFrame:

    logger = logging.getLogger(__name__)
    logger.info("Cleaning outcomes")

    df = df.copy()

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df["month"] = pd.to_datetime(df["month"], errors = "coerce")

    df["has_crime_id"] = df["crime_id"].notna()
    df["has_location"] = df["latitude"].notna() & df["longitude"].notna()

    df["outcome_type"] = df["outcome_type"].astype("string").str.strip()

    before_dedupe = len(df)
    logger.info(f"outcomes rows before dedupe: {before_dedupe}")

    df = df.drop_duplicates(
        subset = ["crime_id", "month", "outcome_type"],
        keep = "first",
        ignore_index = True
    )

    after_dedupe = len(df)
    rows_dropped = before_dedupe - after_dedupe

    logger.info(f"outcomes rows after dedupe: {after_dedupe}")
    logger.info(f"outcomes rows dropped: {rows_dropped}")

    logger.info(f"Cleaning complete outcomes rows: {len(df)}")

    return df
