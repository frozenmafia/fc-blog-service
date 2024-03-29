"""comment table updated

Revision ID: 1cb9a2ae8ade
Revises: 1ebf396c5177
Create Date: 2024-02-27 20:43:49.796994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cb9a2ae8ade'
down_revision: Union[str, None] = '1ebf396c5177'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.String(), nullable=False))
    op.drop_column('comments', 'content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###
