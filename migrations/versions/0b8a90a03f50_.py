"""empty message

Revision ID: 0b8a90a03f50
Revises: 
Create Date: 2018-03-19 01:13:22.018923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b8a90a03f50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jingfen_class',
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jd_uid', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('sub_name', sa.String(length=128), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('pic_url', sa.String(length=128), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('content_skus', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jd_uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('jingfen_products',
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('sku', sa.String(length=128), nullable=True),
    sa.Column('spu', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('bonus_rate', sa.Float(), nullable=False),
    sa.Column('prize_amout', sa.Float(), nullable=False),
    sa.Column('image_url', sa.String(length=128), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('link', sa.String(length=128), nullable=True),
    sa.Column('ticket_id', sa.String(length=128), nullable=True),
    sa.Column('ticket_total_number', sa.Integer(), nullable=True),
    sa.Column('ticket_used_number', sa.Integer(), nullable=True),
    sa.Column('ticket_amount', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('ticket_valid', sa.Boolean(), nullable=True),
    sa.Column('good_come', sa.Integer(), nullable=True),
    sa.Column('jingfen_class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['jingfen_class_id'], ['jingfen_class.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('spu')
    )
    op.create_index(op.f('ix_jingfen_products_id'), 'jingfen_products', ['id'], unique=False)
    op.create_index(op.f('ix_jingfen_products_sku'), 'jingfen_products', ['sku'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_jingfen_products_sku'), table_name='jingfen_products')
    op.drop_index(op.f('ix_jingfen_products_id'), table_name='jingfen_products')
    op.drop_table('jingfen_products')
    op.drop_table('jingfen_class')
    # ### end Alembic commands ###
