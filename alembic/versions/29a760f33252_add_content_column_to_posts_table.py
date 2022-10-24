"""add content column to posts table

Revision ID: 29a760f33252
Revises: a2b8bcd9a9d1
Create Date: 2022-10-24 09:59:12.126241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a760f33252'
down_revision = 'a2b8bcd9a9d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
