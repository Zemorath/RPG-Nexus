"""Added attributes to spell table for system specific attributes

Revision ID: 0f1d53ad80aa
Revises: 35b36e23c1fa
Create Date: 2024-10-20 12:31:40.347262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f1d53ad80aa'
down_revision = '35b36e23c1fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('force_power_tree', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('strain_cost', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('conflict_risk', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.drop_column('conflict_risk')
        batch_op.drop_column('strain_cost')
        batch_op.drop_column('force_power_tree')
        batch_op.drop_column('type')

    # ### end Alembic commands ###
