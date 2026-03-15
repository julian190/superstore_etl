import pandas as pd
import sqlite3 as sql
import os
def load_data(df: pd.DataFrame, output_path: str,sqlite_db_path: str):
    """Load the cleaned data to the sqlite."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    #Load data to sqlite
    conn = sql.connect(sqlite_db_path)
    print(sqlite_db_path)
    df.to_sql("cleaned_superstore", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"Data successfully saved to {output_path}")
    print(f"Data successfully loaded to database file {sqlite_db_path}")
