"""create table creditcards

Revision ID: 33e89441535f
Revises: 
Create Date: 2023-09-23 13:11:28.030917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33e89441535f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('creditcards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('holder', sa.String(), nullable=True),
    sa.Column('number', sa.String(), nullable=True),
    sa.Column('exp_date', sa.Date(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('creditcards')
    # ### end Alembic commands ###