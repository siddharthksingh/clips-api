from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    genre = Column(String)
    duration = Column(String)
    audio_url = Column(String)
    play_count = Column(Integer, default=0)
