"""added foreign keys to class, race, item, monster and skill for rpg system

Revision ID: 18fe1c8fa7c0
Revises: 92acde334dd6
Create Date: 2024-09-03 20:30:42.830709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18fe1c8fa7c0'
down_revision = '92acde334dd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rpg_system_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_class_rpg_system_id', 'rpg_system', ['rpg_system_id'], ['id'])

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rpg_system_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_item_rpg_system_id', 'rpg_system', ['rpg_system_id'], ['id'])

    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rpg_system_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_race_rpg_system_id', 'rpg_system', ['rpg_system_id'], ['id'])

    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rpg_system_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_skill_rpg_system_id', 'rpg_system', ['rpg_system_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rpg_system_id')

    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rpg_system_id')

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rpg_system_id')

    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rpg_system_id')

    # ### end Alembic commands ###
