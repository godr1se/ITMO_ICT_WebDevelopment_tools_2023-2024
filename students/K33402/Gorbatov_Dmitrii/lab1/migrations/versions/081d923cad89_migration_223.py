"""migration_223

Revision ID: 081d923cad89
Revises: 
Create Date: 2024-08-25 17:03:57.364575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '081d923cad89'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('timelog', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('timelog', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
