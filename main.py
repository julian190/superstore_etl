import os
import yaml
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def main():
    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    source_file = config["source"]["file_path"]
    output_file = os.path.join("data", "processed", "cleaned_superstore.csv")
    output_db = config["database"]["connection_string"]
    
    print("Extracting data...")
    df = extract_data(source_file, encoding=config["source"]["encoding"])
    
    print("Transforming data...")
    df_clean = transform_data(df)
    
    print("Loading data...")
    load_data(df_clean, output_file,output_db)
    
    print("ETL process completed successfully!")
    #print(df_clean.head())

if __name__ == "__main__":
    main()
