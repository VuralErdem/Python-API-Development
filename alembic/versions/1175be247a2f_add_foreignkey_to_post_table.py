"""add foreignkey to post table

Revision ID: 1175be247a2f
Revises: f41cbc7da094
Create Date: 2022-10-24 10:12:25.495327

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1175be247a2f'
down_revision = 'f41cbc7da094'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
