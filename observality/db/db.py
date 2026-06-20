import os
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
    Engine
)


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://root:root@localhost:5433/observability"
)


metadata = MetaData()


email_events = Table(
    "email_events",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created_at", DateTime(timezone=True), nullable=False,),
    Column("level", String(20), nullable=False,),
    Column("logger", String(100), nullable=True,),
    Column("event", String(100), nullable=False,),
    Column("message", Text, nullable=False,),
    Column("recipient", String(255), nullable=True,),
    Column("subject", String(255), nullable=False,),
    Column("duration_ms", Float, nullable=True,),
    Column("cpu_percent", Float, nullable=True,),
    Column("memory_percent", Float, nullable=True,),
    Column("process_memory_mb", Float, nullable=True,),
    Column("error", Text, nullable=False,),
    Column("file", String(255), nullable=True,),
    Column("line", Integer, nullable=True,),
    Column("function", String(255), nullable=True,),
    Column("extra", Text, nullable=True,),
)


def get_engine() -> Engine:
    return create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
    )


def create_tables() -> None:
    engine = get_engine()
    metadata.create_all(engine, checkfirst=True,)

def utc_now() -> datetime:
    return datetime.now(timezone.utc)
