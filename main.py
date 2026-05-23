import os
import yaml
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    # Load configuration
    logging.info("Open the config file")
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    source_file = config["source"]["file_path"]
    output_file = os.path.join("data", "processed", "cleaned_superstore.csv")
    output_db = config["database"]["connection_string"]
    
    logging.info("Extracting data...")
    df = extract_data(source_file, encoding=config["source"]["encoding"])
    
    logging.info("Transforming data...")
    df_clean = transform_data(df)
    
    logging.info("Loading data...")
    load_data(df_clean, output_file,output_db)
    
    logging.info("ETL process completed successfully!")
    #print(df_clean.head())

if __name__ == "__main__":
    main()
