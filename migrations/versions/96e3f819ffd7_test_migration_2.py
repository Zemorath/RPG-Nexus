"""Test Migration 2

Revision ID: 96e3f819ffd7
Revises: 4a5e91b89db9
Create Date: 2024-09-10 20:24:44.028653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96e3f819ffd7'
down_revision = '4a5e91b89db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.VARCHAR(length=10), nullable=True))

    # ### end Alembic commands ###
