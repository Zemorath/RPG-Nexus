"""changes to the class models

Revision ID: b9d2183f7257
Revises: d53b882cdd75
Create Date: 2024-09-10 21:53:13.585918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9d2183f7257'
down_revision = 'd53b882cdd75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character_class')
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_character_class_id'), 'class', ['class_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_character_class_id'), type_='foreignkey')
        batch_op.drop_column('class_id')

    op.create_table('character_class',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('character_id', sa.INTEGER(), nullable=False),
    sa.Column('class_id', sa.INTEGER(), nullable=False),
    sa.Column('system_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], name='fk_character_class_character_id'),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], name='fk_character_class_class_id'),
    sa.ForeignKeyConstraint(['system_id'], ['rpg_system.id'], name='fk_character_class_system_id'),
    sa.PrimaryKeyConstraint('id', name='pk_character_class')
    )
    # ### end Alembic commands ###