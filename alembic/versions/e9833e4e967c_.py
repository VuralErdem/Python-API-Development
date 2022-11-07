"""empty message

Revision ID: e9833e4e967c
Revises: 1175be247a2f
Create Date: 2022-10-24 10:19:29.677205

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9833e4e967c'
down_revision = '1175be247a2f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
