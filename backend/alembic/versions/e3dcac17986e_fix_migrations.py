"""fix_migrations

Revision ID: e3dcac17986e
Revises: 2ba4c48ff4c8
Create Date: 2024-07-12 02:50:52.120044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3dcac17986e'
down_revision: Union[str, None] = '2ba4c48ff4c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user_answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['question_answer.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('email', sa.String(), nullable=False))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')


def downgrade() -> None:
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'email')
    op.drop_table('user_answer')
