"""rename_table

Revision ID: 06b945bab9c8
Revises: 8c619a2bf122
Create Date: 2023-09-06 11:14:38.690540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06b945bab9c8'
down_revision: Union[str, None] = '8c619a2bf122'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
            alter table posts rename to foziljon
        """

    ))



def downgrade() -> None:
    pass
