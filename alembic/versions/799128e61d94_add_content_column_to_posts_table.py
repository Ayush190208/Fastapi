"""add content column to posts table

Revision ID: 799128e61d94
Revises: e6b7c606e51f
Create Date: 2026-06-16 01:51:02.428679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '799128e61d94'
down_revision: Union[str, Sequence[str], None] = 'e6b7c606e51f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
