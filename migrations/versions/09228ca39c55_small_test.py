"""small test

Revision ID: 09228ca39c55
Revises: 0f1d53ad80aa
Create Date: 2024-11-12 22:26:16.621004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09228ca39c55'
down_revision = '0f1d53ad80aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.String(length=10), nullable=True))

    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.alter_column('force_power_tree',
               existing_type=sa.TEXT(),
               type_=sa.JSON(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.alter_column('force_power_tree',
               existing_type=sa.JSON(),
               type_=sa.TEXT(),
               existing_nullable=True)

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###
