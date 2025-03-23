from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '06e9c75e3db6'
down_revision = 'fee39bcacd13'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('pepper_plant', schema=None) as batch_op:
        batch_op.alter_column(
            'dead',
            existing_type=sa.Boolean(),
            type_=sa.Integer(),
            postgresql_using="CASE WHEN dead THEN 1 ELSE 0 END"
        )
        # If there are additional alterations (like adding the fruits column), include them here.
        # batch_op.add_column(sa.Column('fruits', sa.Integer(), nullable=False, server_default="0"))

def downgrade():
    with op.batch_alter_table('pepper_plant', schema=None) as batch_op:
        batch_op.drop_column('fruits')
        batch_op.alter_column(
            'dead',
            existing_type=sa.Integer(),
            type_=sa.Boolean(),
            postgresql_using="CASE WHEN dead = 1 THEN TRUE ELSE FALSE END"
        )
