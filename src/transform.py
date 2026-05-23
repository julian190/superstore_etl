import pandas as pd
import logging
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform the Superstore dataset."""
    try:
        #Handle missing values
        df["Ship Mode"] = df["Ship Mode"].fillna("Unknown")
        df["Customer Name"] = df["Customer Name"].fillna("Unknown")
        df["Segment"] = df["Segment"].fillna("Unknown")
        df["Country"] = df["Country"].fillna("Unknown")
        df["City"] = df["City"].fillna("Unknown")
        df["State"] = df["State"].fillna("Unknown")
        df["Region"] = df["Region"].fillna("Unknown")
        df["Postal Code"] = df["Postal Code"].fillna("Unknown")
        df["Product ID"] = df["Product ID"].fillna("Unknown")
        df["Category"] = df["Category"].fillna("Unknown")
        df["Sub-Category"] = df["Sub-Category"].fillna("Unknown")
        df["Product Name"] = df["Product Name"].fillna("Unknown")
        df["Sales"] = df["Sales"].fillna(0)
        df["Quantity"] = df["Quantity"].fillna(0)
        df["Discount"] = df["Discount"].fillna(0)
        df["Profit"] = df["Profit"].fillna(0)

        # Remove duplicates
        df = df.drop_duplicates()
        
        # Change type to date time for date columns
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
        df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
        
        # Trim the strings 
        df["Customer Name"] = df["Customer Name"].str.strip()
        
        #
        # Standardize text values 
        df["Country"] = df["Country"].str.title()
        df["City"] = df["City"].str.title()
        df["State"] = df["State"].str.title()
        df["Region"] = df["Region"].str.title()

        #Validate data logic 
        logging.info(((df["Sales"] < 0) | (df["Quantity"] < 0) ).sum(), "Invalid values found in Sales or Quantity columns")
    
        df = df[(df["Sales"]>0) & (df["Quantity"]>0)]
        # Make the columns name ready for export to Database 
        df = df.drop(columns=["Row ID"])
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        
        return df
    except Exception as ex:
        logging.error(f"There is an error while transforming data Error {ex}")
