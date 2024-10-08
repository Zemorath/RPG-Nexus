"""added table relationships for class and race to character table

Revision ID: f42b865234e5
Revises: 01d64866767a
Create Date: 2024-09-12 11:03:36.942243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f42b865234e5'
down_revision = '01d64866767a'
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
