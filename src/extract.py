import pandas as pd
import logging
def extract_data(file_path: str, encoding: str = "utf-8") -> pd.DataFrame:
    """Extract Superstore data from the given csv path."""
    try:
        logging.info(f"Read Data from CSV file {file_path}")
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as ex:
        logging.info(f"There is an error while extracting from CSV {file_path} error {ex}")
        ex
   
