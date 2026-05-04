import pandas as pd
import logging

def build_latest_outcomes(df: pd.DataFrame) -> pd.DataFrame:

    logger = logging.getLogger(__name__)
    logger.info("Building latest outcomes")

    df = df.copy()

    df["month"] = pd.to_datetime(df["month"], errors = "coerce")

    df = df.sort_values("month")

    before_dedupe = len(df)
    logger.info(f"latest outcomes rows before dedupe: {before_dedupe}")

    df = df.drop_duplicates(
        subset = ["crime_id"],
        keep = "last",
        ignore_index = True
    )

    after_dedupe = len(df)
    logger.info(f"latest outcomes rows after dedupe: {after_dedupe}")

    df = df.rename(columns = {
        "month": "latest_outcome_month",
        "outcome_type": "latest_outcome_type"
    })

    df = df.loc[:, [
        "crime_id",
        "latest_outcome_month",
        "latest_outcome_type"
    ]].copy()

    logger.info(f"Latest outcomes rows: {len(df)}")

    return df
