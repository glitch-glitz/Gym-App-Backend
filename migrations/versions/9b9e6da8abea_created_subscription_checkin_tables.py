"""Created Subscription & CheckIn Tables

Revision ID: 9b9e6da8abea
Revises: 926eaf81a3b9
Create Date: 2025-06-01 19:59:33.965905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b9e6da8abea'
down_revision: Union[str, None] = '926eaf81a3b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('check_ins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('check_in_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('plan_name', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('members', sa.Column('full_name', sa.String(), nullable=False))
    op.add_column('members', sa.Column('weight', sa.Float(), nullable=True))
    op.add_column('members', sa.Column('bmi', sa.Float(), nullable=True))
    op.add_column('members', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column('members', 'starting_weight')
    op.drop_column('members', 'height')
    op.drop_column('members', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('name', sa.TEXT(), nullable=False))
    op.add_column('members', sa.Column('height', sa.FLOAT(), nullable=True))
    op.add_column('members', sa.Column('starting_weight', sa.FLOAT(), nullable=True))
    op.drop_column('members', 'created_at')
    op.drop_column('members', 'bmi')
    op.drop_column('members', 'weight')
    op.drop_column('members', 'full_name')
    op.drop_table('subscriptions')
    op.drop_table('check_ins')
    # ### end Alembic commands ###
