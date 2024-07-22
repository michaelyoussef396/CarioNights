"""created payment request table

Revision ID: d98b7697e535
Revises: 9bad1ca0e5ae
Create Date: 2024-07-23 03:44:58.545948

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd98b7697e535'
down_revision: Union[str, None] = '9bad1ca0e5ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    if not op.get_bind().dialect.has_table(op.get_bind(), 'payment_requests'):
        op.create_table(
            'payment_requests',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('table_number', sa.Integer, sa.ForeignKey('restaurant_tables.id'), nullable=False),
            sa.Column('timestamp', sa.DateTime, default=sa.func.now()),
            sa.Column('status', sa.String, default='Pending'),
            sa.Column('total_amount', sa.Float, nullable=False),
        )

def downgrade() -> None:
    op.drop_table('payment_requests')
