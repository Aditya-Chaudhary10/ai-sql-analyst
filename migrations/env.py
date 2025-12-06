from logging.config import fileConfig
import sys
from pathlib import Path
import backend.models

from alembic import context
from sqlalchemy import engine_from_config, pool

# -----------------------------
# FIX: Add project root to PYTHONPATH
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

# -----------------------------
# Import Base AFTER fixing sys.path
# -----------------------------
from backend.models.base import Base

# This tells Alembic where models metadata is stored
target_metadata = Base.metadata

config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)



def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
