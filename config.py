import os
import secrets
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    try:
        # Load OpenAI API key
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing. Ensure it is set in environment variables or config.")

        # Generate a random secret key for Flask
        SECRET_KEY = secrets.token_hex(16)

        # Database configuration
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///chat_history.db")
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    except Exception as e:
        # Handle configuration errors
        print(f"Error in configuration: {e}")
        raise
