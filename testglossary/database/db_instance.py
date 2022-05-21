
# Database Dependency
from testglossary.database import connection


def use_db():
    """"Generate an instance of database connection to be used."""
    
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()
