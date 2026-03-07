from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.events import Event
from schemas.event import EventCreate


def create_event(current_user, event: EventCreate, db: Session):

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized user"
        )

    try:
        breakpoint()
        new_event = Event(
            title=event.title,
            description=event.description,
            location=event.location,
            start_date=event.start_date,
            end_date=event.end_date,
            expected_guests=event.expected_guests,
            created_by=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            form_fields=[field.dict() for field in event.fields]
        )

        db.add(new_event)
        db.commit()
        db.refresh(new_event)

        return {
            "message": "Event created successfully",
            "event_id": new_event.id
        }

    except Exception as e:
        print(f"Error creating event: {e}")
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create event"
        )


def get_all_events(current_user, db: Session):
    """Get all events created by the logged-in user"""
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized user"
        )

    try:
        events = db.query(Event).filter(Event.created_by == current_user.id).all()
        return events

    except Exception as e:
        print(f"Error fetching events: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch events"
        )