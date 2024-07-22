"""drop payment_requests table

Revision ID: 931f04c56a80
Revises: <new_revision_id>
Create Date: 2024-07-23 04:36:58.157977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '931f04c56a80'
down_revision: Union[str, None] = '<new_revision_id>'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop the payment_requests table
    op.drop_table('payment_requests')

def downgrade():
    # Recreate the payment_requests table in case of downgrade
    op.create_table(
        'payment_requests',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('table_number', sa.Integer, sa.ForeignKey('restaurant_tables.id'), nullable=False),
        sa.Column('timestamp', sa.DateTime, default=sa.func.now()),
        sa.Column('status', sa.String, default='Pending'),
        sa.Column('total_amount', sa.Float, nullable=False)
    )