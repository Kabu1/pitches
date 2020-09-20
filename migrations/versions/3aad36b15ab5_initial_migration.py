"""Initial Migration

Revision ID: 3aad36b15ab5
Revises: 428bdfb96116
Create Date: 2020-09-20 12:45:21.428952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aad36b15ab5'
down_revision = '428bdfb96116'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
