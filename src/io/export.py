import pandas as pd
from pathlib import Path
import logging

def export_to_csv(df: pd.DataFrame, output_path: Path, file_name: str):
    logger = logging.getLogger(__name__)

    output_path.mkdir(parents = True, exist_ok = True)
    df.to_csv(output_path / file_name, index = False)
    
    logger.info(f"Saved {file_name}")