import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

# Database configuration settings
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'wsaa')
}