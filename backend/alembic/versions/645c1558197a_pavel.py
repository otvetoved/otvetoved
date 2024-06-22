"""Pavel

Revision ID: 645c1558197a
Revises: f213ba29a788
Create Date: 2024-06-20 15:35:46.273310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '645c1558197a'
down_revision: Union[str, None] = 'f213ba29a788'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user_session',
    sa.Column('session_token', sa.UUID(), nullable=False),
    sa.Column('session_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.add_column('user', sa.Column('password', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])


def downgrade() -> None:
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_table('user_session')
