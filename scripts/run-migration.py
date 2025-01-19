from sqlalchemy import create_engine, text
from dotenv import load_dotenv  
import os
load_dotenv()

databaseUrl = os.getenv("DATABASE_URL")
engine  = create_engine(databaseUrl,echo=True)

with engine.connect() as connection:
    queries = [
        """
        CREATE TABLE IF NOT EXISTS USERS (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            refresh_token VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS TASKS (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            user_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES USERS(id) ON DELETE CASCADE
        )
        """
    ]
    
    for query in queries:
        connection.execute(text(query))
    connection.commit()