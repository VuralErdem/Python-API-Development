"""create posts table

Revision ID: a2b8bcd9a9d1
Revises: 
Create Date: 2022-10-24 09:38:45.807821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2b8bcd9a9d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
    pass
