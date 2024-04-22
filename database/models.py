import uuid
from sqlalchemy import String, DateTime, Column, func
from sqlalchemy.dialects.postgresql import UUID
from ascend.database import Base


class BaseModel(Base):
    """
    Base Class for shared columns.
    """

    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(BaseModel):
    """
    User Model
    """

    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
