"""moved the join table from user and campaign to character and campaign for better structure

Revision ID: c4db8c88b3aa
Revises: 7d4c09e90af9
Create Date: 2024-09-01 12:04:09.282232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4db8c88b3aa'
down_revision = '7d4c09e90af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character_campaign',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.PrimaryKeyConstraint('character_id', 'campaign_id')
    )
    op.drop_table('campaign_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('campaign_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('role', sa.VARCHAR(length=20), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('character_campaign')
    # ### end Alembic commands ###