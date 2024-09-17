"""empty message

Revision ID: 323ceaea68c2
Revises: e29fc7ea9dd2
Create Date: 2024-09-16 16:56:04.255529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323ceaea68c2'
down_revision = 'e29fc7ea9dd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint('fk_character_class_progression_id', type_='foreignkey')
        batch_op.drop_column('class_progression_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_progression_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_character_class_progression_id', 'class_progression', ['class_progression_id'], ['id'])

    # ### end Alembic commands ###
