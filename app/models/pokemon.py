from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255))
    types: list[str] = Column(JSONB)
    images: dict[str, str] = Column(JSONB)
