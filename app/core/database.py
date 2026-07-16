import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "hospital_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def ensure_database_exists() -> bool:
    server_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    try:
        server_engine = create_engine(server_url, pool_pre_ping=True)
        with server_engine.begin() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))
        return True
    except SQLAlchemyError:
        return False


def init_db() -> bool:
    try:
        if not ensure_database_exists():
            return False

        from app.model.patients import Patients  # noqa: F401

        Base.metadata.create_all(bind=engine)
        return True
    except SQLAlchemyError:
        return False


def get_db() -> Generator:
    db = SessionLocal()
    try:
        init_db()
        yield db
    finally:
        db.close()
