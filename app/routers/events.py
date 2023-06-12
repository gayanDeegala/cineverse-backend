from fastapi import APIRouter, HTTPException
from app.database.connection import create_mysql_connection
import json

from app.database.event import get_all_events, get_event_info

router = APIRouter()


# API endpoint to get all events
@router.get('/events')
async def get_events():
    events = get_all_events()

    if events:
        return events
    else:
        raise HTTPException(status_code=404, detail='No events found')


@router.get('/events/{date}/{show_time}/{theatre}')
async def get_event(date: str, show_time: str, theatre: str):
    event = get_event_info(date, show_time, theatre)

    if event:
        return event
    else:
        raise HTTPException(status_code=404, detail='Event not found')


