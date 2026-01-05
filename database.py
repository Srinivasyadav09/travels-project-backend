from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Use DATABASE_URL from environment (e.g. set in Vercel). Fall back to local SQLite for dev.
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./bookings.db")

# For SQLite we need `check_same_thread`; other DBs (Postgres, MySQL) don't use it.
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
