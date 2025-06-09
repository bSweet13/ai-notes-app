from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def create_dbs():
    # URLs without database name
    base_url = "postgresql://postgres:postgres@localhost:5432/"
    
    # Database names
    databases = ['ai_notes_dev', 'ai_notes_test']
    
    for db_name in databases:
        db_url = f"{base_url}{db_name}"
        engine = create_engine(db_url)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print(f"Database {db_name} created successfully!")
        else:
            print(f"Database {db_name} already exists!")

if __name__ == "__main__":
    create_dbs() 