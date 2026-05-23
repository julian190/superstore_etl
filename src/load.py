import pandas as pd
import sqlite3 as sql
import os
import logging
def load_data(df: pd.DataFrame, output_path: str,sqlite_db_path: str):
    """Load the cleaned data to the sqlite."""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        
        #Load data to sqlite
        conn = sql.connect(sqlite_db_path)
        logging.info(sqlite_db_path)
        df.to_sql("cleaned_superstore", conn, if_exists="replace", index=False)
        conn.close()
        
        logging.info(f"Data successfully saved to {output_path}")
        logging.info(f"Data successfully loaded to database file {sqlite_db_path}")
    except Exception as  ex:
        logging.error("There is an error while loading to the database {sqlite_db_path} Error: {ex}")