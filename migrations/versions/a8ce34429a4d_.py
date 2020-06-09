"""empty message

Revision ID: a8ce34429a4d
Revises: 2fcb9691e42c
Create Date: 2020-06-09 12:17:53.251118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ce34429a4d'
down_revision = '2fcb9691e42c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('author', sa.String(length=128), nullable=True),
    sa.Column('publisher_name', sa.String(length=128), nullable=True),
    sa.Column('sales_date', sa.String(length=128), nullable=True),
    sa.Column('medium_image_url', sa.String(length=128), nullable=True),
    sa.Column('donor', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###