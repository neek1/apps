"""empty message

Revision ID: 5670094640f7
Revises: fe69fee355a7
Create Date: 2022-07-30 04:45:16.314912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5670094640f7'
down_revision = 'fe69fee355a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders_products',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('cust_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['cust_id'], ['customers.cust_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.PrimaryKeyConstraint('order_id', 'cust_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_products')
    # ### end Alembic commands ###