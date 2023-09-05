"""empty message

Revision ID: aac6fa6af7a9
Revises: 
Create Date: 2023-09-05 15:58:55.802419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aac6fa6af7a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('spots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spot_name', sa.String(length=55), nullable=False),
    sa.Column('address', sa.String(length=55), nullable=False),
    sa.Column('city', sa.String(length=55), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cover_photo', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('spot_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spots')
    op.drop_table('users')
    # ### end Alembic commands ###