"""add foreign-key to posts table

Revision ID: b0ab11449f49
Revises: 7167eb65cd1d
Create Date: 2026-06-17 00:48:07.885941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0ab11449f49'
down_revision: Union[str, Sequence[str], None] = '7167eb65cd1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE"
                          )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
