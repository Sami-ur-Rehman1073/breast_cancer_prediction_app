from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for SQLAlchemy models
Base = declarative_base()


def get_db():
    """
    Creates a database session.

    This function is used inside FastAPI endpoints.
    It automatically closes the session after the request finishes.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()