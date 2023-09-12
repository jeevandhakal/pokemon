from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv

load_dotenv()  

class Settings(BaseModel):
    database_url: str = getenv("DB_URL")
    debug: bool = getenv("DEBUG", "False") == "True"

settings = Settings()