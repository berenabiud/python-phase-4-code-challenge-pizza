"""created relationships

Revision ID: 7abafb410958
Revises: 
Create Date: 2025-01-26 18:54:02.495705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7abafb410958'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], name=op.f('fk_restaurant_pizzas_pizza_id_pizzas')),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], name=op.f('fk_restaurant_pizzas_restaurant_id_restaurants')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_pizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
    # ### end Alembic commands ###
