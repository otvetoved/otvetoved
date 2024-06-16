"""Initial

Revision ID: f213ba29a788
Revises: 
Create Date: 2024-06-16 01:07:08.698461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f213ba29a788'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_by_user_id', sa.Integer(), nullable=True),
    sa.Column('brief', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['created_by_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table("question_tag")
    op.drop_table("question_answer")
    op.drop_table("question")
    op.drop_table("user")
    op.drop_table("tag")
