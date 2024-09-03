"""Tabela ranking

Revision ID: 4ebbfb9e7bf6
Revises: 81d9c68ac453
Create Date: 2024-09-03 18:19:43.031176

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ebbfb9e7bf6'
down_revision: Union[str, None] = '81d9c68ac453'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ranking',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('regiao', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('regiao')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ranking')
    # ### end Alembic commands ###
