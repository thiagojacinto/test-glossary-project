from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from testglossary.internal.config import configuration

# from FastAPI docs' https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-parts

engine = create_engine(
    url=configuration.DATABASE_CONNECTION_STRING, pool_pre_ping=True, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
