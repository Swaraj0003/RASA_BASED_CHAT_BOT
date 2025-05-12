from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.base import Base

DATABASE_URL = "sqlite:///etqan_chatbot.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    from backend.models.user import User
    Base.metadata.create_all(bind=engine)
