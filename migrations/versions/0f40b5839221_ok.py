"""ok

Revision ID: 0f40b5839221
Revises: 
Create Date: 2019-01-13 12:17:17.370488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f40b5839221'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('record_serial_number', sa.String(length=16), nullable=False),
    sa.Column('record_type', sa.Boolean(), nullable=False),
    sa.Column('record_post_date', sa.String(length=64), nullable=False),
    sa.Column('record_software_version', sa.String(length=16), nullable=False),
    sa.Column('record_order', sa.Integer(), nullable=False),
    sa.Column('record_manufacturer', sa.String(length=4), nullable=False),
    sa.Column('record_state', sa.Integer(), nullable=False),
    sa.Column('record_file_uri', sa.String(length=128), nullable=False),
    sa.Column('record_file_name', sa.String(length=64), nullable=True),
    sa.Column('record_inspector', sa.String(length=32), nullable=False),
    sa.Column('record_test', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('register_time', sa.String(length=40), nullable=True),
    sa.Column('toggle', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('records')
    # ### end Alembic commands ###