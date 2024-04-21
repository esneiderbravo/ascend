"""
DB Setup
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ascend.app import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()


class DBContextManager:
    """
    DB context manager
    """

    def __init__(self):
        self.db_instance = SessionLocal()

    def __enter__(self):
        return self.db_instance

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_instance.close()
