from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def get_connection():
    hostname = 'localhost'
    database = 'Med'
    username = 'postgres'
    pwd = '2525'
    port_id = '5432'

    # Construct the database URL required by SQLAlchemy
    db_url = f'postgresql+psycopg2://{username}:{pwd}@{hostname}:{port_id}/{database}'

    try:
        # Create an SQLAlchemy engine
        engine = create_engine(db_url)
        
        # Test the connection by establishing it temporarily
        with engine.connect() as connection:
            print("Connection successful")
        
        # Return the engine to be used with pandas
        return engine
    except OperationalError as e:
        print("OperationalError:", e)
    except Exception as e:
        print("Error connecting to the database:", e)
    return None

def export_to_Postgres(df, table_name):
    """
    Exports the DataFrame to a PostgreSQL database table.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be exported.
        table_name (str): The name of the table to store the data in PostgreSQL.
    """
    engine = get_connection()
    
    if engine is not None:
        try:
            # Export the DataFrame to the PostgreSQL table
            df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
            print(f"Table '{table_name}' has been successfully exported to the PostgreSQL database.")
        except Exception as e:
            print("Error exporting data:", e)
    else:
        print("Failed to establish a database connection.")