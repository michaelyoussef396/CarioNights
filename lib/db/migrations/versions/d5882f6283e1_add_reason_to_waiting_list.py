"""add reason to waiting list

Revision ID: d5882f6283e1
Revises: d98b7697e535
Create Date: 2024-07-23 03:45:41.665506

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = 'd5882f6283e1'
down_revision: Union[str, None] = 'd98b7697e535'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def column_exists(table_name, column_name):
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    columns = [col['name'] for col in inspector.get_columns(table_name)]
    return column_name in columns


def upgrade() -> None:
    if not column_exists('waiting_list', 'reason'):
        op.add_column('waiting_list', sa.Column('reason', sa.String(), nullable=False, server_default='Seating'))
    if not column_exists('waiting_list', 'timestamp'):
        op.add_column('waiting_list', sa.Column('timestamp', sa.DateTime(), nullable=False, server_default=sa.func.now()))
    if not column_exists('waiting_list', 'status'):
        op.add_column('waiting_list', sa.Column('status', sa.String(), nullable=False, server_default='Waiting'))


def downgrade() -> None:
    if column_exists('waiting_list', 'status'):
        op.drop_column('waiting_list', 'status')
    if column_exists('waiting_list', 'timestamp'):
        op.drop_column('waiting_list', 'timestamp')
    if column_exists('waiting_list', 'reason'):
        op.drop_column('waiting_list', 'reason')