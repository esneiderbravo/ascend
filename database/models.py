"""
DB Models
"""
import uuid
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.sql.schema import Column
from ascend.database import Base


class BaseModel(Base):
    """
    Base Class for shared columns.
    """

    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class User(BaseModel):
    """
    User Model
    """

    __tablename__ = "user"

    id = Column(String, primary_key=True, default=uuid.uuid4())
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
