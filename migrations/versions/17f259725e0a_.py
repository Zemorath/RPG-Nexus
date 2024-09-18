"""empty message

Revision ID: 17f259725e0a
Revises: fd6d085384b2
Create Date: 2024-09-17 20:46:13.325704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17f259725e0a'
down_revision = 'fd6d085384b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('background_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('alignment_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_character_background_id'), 'background', ['background_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_character_alignment_id'), 'alignment', ['alignment_id'], ['id'])
        batch_op.drop_column('alignment')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('alignment', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_character_alignment_id'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_character_background_id'), type_='foreignkey')
        batch_op.drop_column('alignment_id')
        batch_op.drop_column('background_id')

    # ### end Alembic commands ###
