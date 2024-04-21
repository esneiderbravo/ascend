"""
User schema for data validation and serialization
"""
import uuid

from pydantic import BaseModel, Field
from pydantic.schema import datetime


class UserSchema(BaseModel):
    """
    Schema for User data
    """

    id: str = Field(default_factory=uuid.uuid4, example=str(uuid.uuid4()))
    username: str = Field(example="johndoe@gmail.com")
    email: str = Field(example="johndoe@gmail.com")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, example=datetime.utcnow()
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, example=datetime.utcnow()
    )
