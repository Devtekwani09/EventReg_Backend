from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class FormOption(BaseModel):
    label: str
    value: str

class FormField(BaseModel):
    type: str
    label: str
    required: bool = False
    placeholder: Optional[str] = None
    options: Optional[List[FormOption]] = None

class EventCreate(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    location: str
    expected_guests: Optional[int] = None
    fields: List[FormField]

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    start_date: datetime
    end_date: datetime
    expected_guests: Optional[int]
    created_by: int
    created_at: datetime
    updated_at: datetime
    form_fields: Optional[List] = None

    class Config:
        from_attributes = True