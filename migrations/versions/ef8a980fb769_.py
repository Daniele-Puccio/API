"""empty message

Revision ID: ef8a980fb769
Revises: 85e86510bc7d
Create Date: 2022-11-02 08:03:38.843464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef8a980fb769'
down_revision = '85e86510bc7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###