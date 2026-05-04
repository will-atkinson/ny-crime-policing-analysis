import logging

from src.io import *
from src.logger import get_logger
from src.cleaning import *
from src.transform import *

def main():
    
    get_logger()
    logger = logging.getLogger(__name__)

    logger.info("Starting pipeline")

    street, outcomes, search = load_data()

    logger.info("Starting cleaning")

    street = clean_street(street)
    outcomes = clean_outcomes(outcomes)
    search = clean_search(search)
    latest_outcomes = build_latest_outcomes(outcomes)

    output_path = Path.cwd() / "data/cleaned"
    
    logger.info("Starting export")

    export_to_csv(street, output_path, "street.csv")
    export_to_csv(outcomes, output_path, "outcomes.csv")
    export_to_csv(search, output_path, "search.csv")
    export_to_csv(latest_outcomes, output_path, "latest_outcomes.csv")

if __name__ == "__main__":
    main()