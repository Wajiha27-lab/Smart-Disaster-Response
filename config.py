import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "smart_disaster_secret")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

    UPLOAD_FOLDER = "uploads"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg"
    }

    DATABASE = "disaster_reports.db"
