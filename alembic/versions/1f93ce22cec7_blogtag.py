"""BlogTag

Revision ID: 1f93ce22cec7
Revises: 93ad8efb9fb1
Create Date: 2024-02-28 01:54:43.109459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f93ce22cec7'
down_revision: Union[str, None] = '93ad8efb9fb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blogs_tags', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('blogs_tags', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blogs_tags', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('blogs_tags', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###