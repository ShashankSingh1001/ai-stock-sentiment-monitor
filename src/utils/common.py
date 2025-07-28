# src/utils/common.py
import os
import pandas as pd
import yaml
from src.exception import CustomException
from src.logger import logging
import sys # Added sys for CustomException

def save_dataframe_to_csv(df: pd.DataFrame, file_path: str, append: bool = True, header: bool = True):
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True) # Ensure directory exists

    try:
        if append and os.path.exists(file_path):
            # Infer datetime column for parsing based on common names
            date_cols = [col for col in ['published_at', 'created_at'] if col in df.columns]
            existing_df = pd.read_csv(file_path, parse_dates=date_cols, errors='coerce')
            
            # Determine subset for de-duplication based on common unique identifiers
            dedup_subset = ['url', 'title'] # Default for news
            if 'tweet_id' in df.columns: # Specific de-duplication for tweets
                dedup_subset = ['tweet_id']

            combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=dedup_subset, keep='first')
            
            # Sort by datetime column if available for consistency
            if 'published_at' in combined_df.columns:
                combined_df.sort_values(by='published_at', ascending=False, inplace=True)
            elif 'created_at' in combined_df.columns:
                combined_df.sort_values(by='created_at', ascending=False, inplace=True)

            combined_df.to_csv(file_path, index=False, header=True) # Always write header for combined
            logging.info(f"Appended and de-duplicated {len(df)} new/updated records. Total unique records: {len(combined_df)} in {file_path}")
        else:
            df.to_csv(file_path, index=False, header=header)
            logging.info(f"Created/overwrote {len(df)} records in {file_path}")
    except Exception as e:
        logging.error(f"Error saving DataFrame to CSV {file_path}: {e}", exc_info=True)
        raise CustomException(f"Error saving CSV: {e}", sys.exc_info())

def load_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Error loading YAML file {file_path}: {e}", exc_info=True)
        raise CustomException(f"Error loading YAML: {e}", sys.exc_info())