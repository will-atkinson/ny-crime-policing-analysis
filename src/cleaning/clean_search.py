import pandas as pd
import logging

def clean_search(df: pd.DataFrame) -> pd.DataFrame:

    logger = logging.getLogger(__name__)
    logger.info("Cleaning search")

    df = df.copy()

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

    df["date"] = pd.to_datetime(df["date"], errors = "coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["time"] = df["date"].dt.hour

    df["has_location"] = df["latitude"].notna() & df["longitude"].notna()

    CATEGORICAL_COLS = [
        "gender", 
        "age_range", 
        "self_defined_ethnicity", 
        "officer_defined_ethnicity", 
        "outcome", 
        "object_of_search", 
        "outcome",
        "legislation"
    ]

    for col in CATEGORICAL_COLS:
        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
            .fillna("Not Specified")
            .replace("", "Not Specified")
        )

    df["outcome_linked_to_object_of_search"] = (
        df["outcome_linked_to_object_of_search"]
        .astype("string")
        .str.strip()
        .str.lower()
        .map({
            "true": "Yes",
            "false": "No",
        })
        .fillna("Not Specified")
    )

    df = df.drop(columns = [
        "part_of_a_policing_operation", 
        "policing_operation", 
        "removal_of_more_than_just_outer_clothing"
    ])

    logger.info(f"Cleaning complete search rows: {len(df)}")

    return df
