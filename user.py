from sqlalchemy import Column, Integer, String
from backend.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    enquiry = Column(String)

