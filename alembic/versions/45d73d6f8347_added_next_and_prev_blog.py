"""added next and prev blog

Revision ID: 45d73d6f8347
Revises: 871fb898e8e4
Create Date: 2024-03-22 22:37:23.484891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45d73d6f8347'
down_revision: Union[str, None] = '871fb898e8e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('next', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('prev', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'prev')
    op.drop_column('blogs', 'next')
    # ### end Alembic commands ###
