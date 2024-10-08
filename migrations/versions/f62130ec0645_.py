"""empty message

Revision ID: f62130ec0645
Revises: 82e0ed2ff81a
Create Date: 2024-09-16 18:09:49.740814

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'f62130ec0645'
down_revision = '82e0ed2ff81a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('class_progression', schema=None) as batch_op:
        batch_op.add_column(sa.Column('available_spell', sa.JSON(), nullable=True))
        batch_op.drop_column('available_spells')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('class_progression', schema=None) as batch_op:
        batch_op.add_column(sa.Column('available_spells', sqlite.JSON(), nullable=True))
        batch_op.drop_column('available_spell')

    # ### end Alembic commands ###
