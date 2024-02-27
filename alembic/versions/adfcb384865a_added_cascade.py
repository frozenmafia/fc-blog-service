"""added cascade

Revision ID: adfcb384865a
Revises: 998fc9eb04a8
Create Date: 2024-02-27 21:50:22.350486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adfcb384865a'
down_revision: Union[str, None] = '998fc9eb04a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###
