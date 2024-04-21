"""Feature - Create User table

Revision ID: d87660a55290
Revises:
Create Date: 2024-01-28 11:00:58.312753

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, DateTime

# revision identifiers, used by Alembic.
revision = "d87660a55290"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """
    Create User table based on the User model.
    """

    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
            primary_key=True,
            default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column("username", String(length=255), nullable=False, unique=True),
        sa.Column("email", String(length=255), nullable=False, unique=True),
        sa.Column("created_at", DateTime(), nullable=False),
        sa.Column("updated_at", DateTime(), nullable=False, onupdate=sa.text("now()")),
    )


def downgrade():
    """
    Rollback all changes
    """
    op.drop_table("user")
