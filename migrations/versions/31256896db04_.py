"""empty message

Revision ID: 31256896db04
Revises: 7aa25c5ee445
Create Date: 2024-09-16 20:49:21.319917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31256896db04'
down_revision = '7aa25c5ee445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.add_column(sa.Column('damage', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.drop_column('damage')

    # ### end Alembic commands ###
