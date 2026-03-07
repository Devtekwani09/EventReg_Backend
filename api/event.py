from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from schemas.event import EventCreate, EventResponse
from services.event_service import create_event, get_all_events
from utils.dependencies import get_current_user

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/new-event", status_code=status.HTTP_201_CREATED)
def new_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        return create_event(current_user, event, db)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while creating the event"
        )

@router.get("/my-events", response_model=List[EventResponse])
def get_my_events(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get all events created by the logged-in user"""
    try:
        return get_all_events(current_user, db)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while fetching events"
        )