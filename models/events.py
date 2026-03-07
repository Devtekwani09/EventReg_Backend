from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from db.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    expected_guests = Column(Integer)
    created_by = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    form_fields = Column(JSON)
