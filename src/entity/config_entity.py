import os
from dataclasses import dataclass # Using dataclasses for concise config classes
from dotenv import load_dotenv # Needed here to load env vars for paths
from pathlib import Path 

ROOT_DIR = Path(__file__).resolve().parents[2] # Go up two levels from config_entity.py

load_dotenv(os.path.join(ROOT_DIR, 'config', '.env'))

@dataclass(frozen=True) # frozen=True makes instances immutable (like a constant)
class DataIngestionConfig:
    # Paths for raw data
    raw_news_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'raw', 'financial_news_raw.csv'))
    static_tweets_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'raw', 'financial_tweets_static.csv'))
    
    # API Key
    marketaux_api_key: str = os.getenv("MARKETAUX_API_KEY")

    # Hardcoded RSS Feeds (can be moved to a separate YAML config if grows large)
    rss_feeds: dict = {
        "Reuters Business": "http://feeds.reuters.com/reuters/businessNews",
        "WSJ Markets": "https://feeds.a.dj.com/rss/RssNewYorkBusiness.xml",
        "Yahoo Finance News (Top Stories)": "https://finance.yahoo.com/news/rss/",
        "Business Standard (Markets)": "https://www.business-standard.com/rss/markets-news",
    }
    
    # Path to stock metadata (though loaded by DataTransformation/ModelTrainer)
    stock_metadata_path: Path = Path(os.path.join(ROOT_DIR, 'config', 'stock_metadata.yaml'))


# @dataclass(frozen=True)
# class DataValidationConfig:
#     # Path for validated data (could be same as raw if no changes, or a new file)
#     validated_news_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'validated', 'validated_news.csv'))
#     validated_tweets_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'validated', 'validated_tweets.csv'))
    
#     # Example: List of expected columns for news data (for validation in Phase 2)
#     required_news_columns: list = ['title', 'description', 'url', 'published_at', 'source']
    



# @dataclass(frozen=True)
# class DataTransformationConfig:
#     # Paths for transformed data
#     transformed_news_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'processed', 'transformed_news.csv'))
#     transformed_tweets_data_path: Path = Path(os.path.join(ROOT_DIR, 'data', 'processed', 'transformed_tweets.csv'))

#     # Configuration for text preprocessing (e.g., stopwords language, lemmatizer model)
#     stopwords_language: str = "english"
    
#     # Configuration for sentiment model (e.g., model name, tokenizer name)
#     # Placeholder for Phase 2/3
#     sentiment_model_name: str = "ProsusAI/finbert" # Example FinBERT model
    
#     # Path to store preprocessor artifacts (e.g., custom tokenizer, if any)
#     preprocessor_artifact_path: Path = Path(os.path.join(ROOT_DIR, 'artifacts', 'preprocessor.pkl'))