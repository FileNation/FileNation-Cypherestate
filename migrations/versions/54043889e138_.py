"""empty message

Revision ID: 54043889e138
Revises: 58ca9a289533
Create Date: 2017-10-15 02:16:45.921363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54043889e138'
down_revision = '58ca9a289533'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    # ### end Alembic commands ###