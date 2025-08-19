"""Add worker_id to Booking

Revision ID: 5842700b866d
Revises: e89e867a8d57
Create Date: 2025-08-15 16:26:21.970444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5842700b866d'
down_revision = 'e89e867a8d57'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('worker_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_booking_worker_id',  # <-- explicit name
            'worker',
            ['worker_id'],
            ['id']
        )


    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_constraint('fk_booking_worker_id', type_='foreignkey')
        batch_op.drop_column('worker_id')


    # ### end Alembic commands ###
