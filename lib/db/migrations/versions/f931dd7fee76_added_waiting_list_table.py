"""added waiting list table

Revision ID: f931dd7fee76
Revises: d5882f6283e1
Create Date: 2024-07-23 03:56:31.713560

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'f931dd7fee76'
down_revision = 'd5882f6283e1'
branch_labels = None
depends_on = None

def table_exists(table_name):
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    return table_name in inspector.get_table_names()

def upgrade():
    if not table_exists('waiting_list'):
        op.create_table(
            'waiting_list',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_name', sa.String(), nullable=False),
            sa.Column('num_people', sa.Integer(), nullable=False),
            sa.Column('reason', sa.String(), nullable=False),
            sa.Column('timestamp', sa.DateTime(), nullable=False, server_default=sa.func.now()),
            sa.Column('status', sa.String(), nullable=False, server_default='Waiting')
        )

def downgrade():
    if table_exists('waiting_list'):
        op.drop_table('waiting_list')
