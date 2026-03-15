import pandas as pd

def extract_data(file_path: str, encoding: str = "utf-8") -> pd.DataFrame:
    """Extract Superstore data from the given csv path."""
    df = pd.read_csv(file_path, encoding=encoding)
    return df
