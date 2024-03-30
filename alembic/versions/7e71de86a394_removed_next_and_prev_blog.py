"""removed next and prev blog

Revision ID: 7e71de86a394
Revises: 45d73d6f8347
Create Date: 2024-03-23 13:16:22.922433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e71de86a394'
down_revision: Union[str, None] = '45d73d6f8347'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'prev')
    op.drop_column('blogs', 'next')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('next', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('prev', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
