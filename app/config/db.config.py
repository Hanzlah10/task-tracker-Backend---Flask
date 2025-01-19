from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()

databaseUrl = os.getenv("DATABASE_URL") 

def execute_query(query):
    try:
        engine = create_engine(databaseUrl)
        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# execute_query(text("SELECT * FROM USERS")) 
