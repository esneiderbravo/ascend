from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class UserSchema(BaseModel):
    """
    Schema for User data
    """

    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique identifier for the user",
    )
    username: str = Field(description="Username of the user")
    email: str = Field(description="Email address of the user")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp indicating when the user was created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp indicating when the user was last updated",
    )

    class Config:
        schema_extra = {
            "example": {
                "id": "f1f8a6db-35fc-47a5-80e4-7a4831a1b48e",
                "username": "johndoe",
                "email": "johndoe@example.com",
                "created_at": "2022-04-25T12:00:00Z",
                "updated_at": "2022-04-25T12:00:00Z",
            }
        }
