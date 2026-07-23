import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)


with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    
    print(result.fetchone())