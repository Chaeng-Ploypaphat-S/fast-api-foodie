import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from a .env file if present

class Settings:
    PROJECT_NAME: str = "FastAPI Foodie"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./foodie.db")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()