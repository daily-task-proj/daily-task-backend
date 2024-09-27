"""empty message

Revision ID: 78d7612a36ee
Revises: 3009d8b13ec4
Create Date: 2024-09-27 07:40:52.015152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d7612a36ee'
down_revision = '3009d8b13ec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('user_team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_team_id'], ['user_teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_team_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('user_groups_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user_teams', ['user_team_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_groups_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_column('user_team_id')

    op.drop_table('user_tasks')
    # ### end Alembic commands ###