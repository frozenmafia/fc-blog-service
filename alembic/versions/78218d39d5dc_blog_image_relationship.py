"""blog image relationship

Revision ID: 78218d39d5dc
Revises: 8081e726daa4
Create Date: 2024-04-07 16:45:19.836736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78218d39d5dc'
down_revision: Union[str, None] = '8081e726daa4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('blog_id', sa.Integer(), nullable=False))
    op.add_column('images', sa.Column('poster_id', sa.Integer(), nullable=False))
    op.drop_constraint('images_blog_fkey', 'images', type_='foreignkey')
    op.create_foreign_key(None, 'images', 'blogs', ['blog_id'], ['id'])
    op.create_foreign_key(None, 'images', 'users', ['poster_id'], ['id'])
    op.drop_column('images', 'blog')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('blog', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.create_foreign_key('images_blog_fkey', 'images', 'blogs', ['blog'], ['id'])
    op.drop_column('images', 'poster_id')
    op.drop_column('images', 'blog_id')
    # ### end Alembic commands ###
