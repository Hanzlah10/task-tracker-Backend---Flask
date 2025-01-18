from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Replace with your actual database connection details
DATABASE_URL = "postgresql://username:242303@localhost:5432/database_name"

def execute_query(query, params=None):
    """
    Execute a SQL query on PostgreSQL database using SQLAlchemy
    
    Args:
        query (str): SQL query to execute
        params (dict): Optional parameters for the query
    
    Returns:
        list: Result of the query if SELECT, or number of affected rows if INSERT/UPDATE/DELETE
    """
    try:
        # Create database engine
        engine = create_engine(DATABASE_URL)
        
        # Execute query with connection
        with engine.connect() as connection:
            if params:
                result = connection.execute(query, params)
            else:
                result = connection.execute(query)
            
            # If SELECT query, fetch all results
            if query.strip().upper().startswith('SELECT'):
                return result.fetchall()
            # For INSERT/UPDATE/DELETE return number of affected rows
            return result.rowcount
            
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None