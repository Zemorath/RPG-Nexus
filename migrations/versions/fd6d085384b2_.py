"""empty message

Revision ID: fd6d085384b2
Revises: d468eb2fd2e4
Create Date: 2024-09-17 20:17:22.749659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6d085384b2'
down_revision = 'd468eb2fd2e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rpg_system_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_alignment_system_id', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_alignment_rpg_system_id'), 'rpg_system', ['rpg_system_id'], ['id'])
        batch_op.drop_column('system_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('system_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_alignment_rpg_system_id'), type_='foreignkey')
        batch_op.create_foreign_key('fk_alignment_system_id', 'rpg_system', ['system_id'], ['id'])
        batch_op.drop_column('rpg_system_id')

    # ### end Alembic commands ###
