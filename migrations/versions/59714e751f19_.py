"""empty message

Revision ID: 59714e751f19
Revises: 0e10e1bf9e50
Create Date: 2024-09-25 14:41:39.574887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59714e751f19'
down_revision = '0e10e1bf9e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('saving_throws', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('skills', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('skills')
        batch_op.drop_column('saving_throws')

    # ### end Alembic commands ###
