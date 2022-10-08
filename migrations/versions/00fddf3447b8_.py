"""empty message

Revision ID: 00fddf3447b8
Revises: df4a7bd12f70
Create Date: 2022-09-03 16:26:33.387922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00fddf3447b8'
down_revision = 'df4a7bd12f70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favourite', sa.Column('ProductFlg', sa.Boolean(), nullable=False))
    op.alter_column('favourite', 'ShopId',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favourite', 'ShopId',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('favourite', 'ProductFlg')
    # ### end Alembic commands ###