"""merge heads

Revision ID: <new_revision_id>
Revises: d5882f6283e1, f931dd7fee76
Create Date: 2024-07-23 10:29:16.435324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '<new_revision_id>'
down_revision: Union[str, None] = ('d5882f6283e1', 'f931dd7fee76')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
