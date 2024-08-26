"""Tabela Time

Revision ID: cedb8953d000
Revises: 10f2ec1cae6b
Create Date: 2024-08-26 14:29:09.450802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cedb8953d000'
down_revision: Union[str, None] = '10f2ec1cae6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('time',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('jogador', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key("fk_jogador_time", 'time', ['time_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jogador', schema=None) as batch_op:
        batch_op.drop_constraint("fk_jogador_time", type_='foreignkey')
        batch_op.drop_column('time_id')

    op.drop_table('time')
    # ### end Alembic commands ###
