from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
database = os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = database
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
