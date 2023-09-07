"""post_title

Revision ID: 8c619a2bf122
Revises: 
Create Date: 2023-09-06 11:09:13.108630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c619a2bf122'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
            alter table posts rename column title to post_title
        """

    ))


def downgrade() -> None:
    pass
