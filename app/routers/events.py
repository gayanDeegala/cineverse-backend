from fastapi import APIRouter, HTTPException
from app.database.event import get_all_events_query, search_event_query, get_event_query

router = APIRouter()


# API endpoint to get all events
@router.get('/events')
async def get_events():
    events = get_all_events_query()

    if events:
        return events
    else:
        raise HTTPException(status_code=404, detail='No events found')


@router.get('/events/{event_id}')
async def get_event_(event_id: int):
    event = get_event_query(event_id)

    if event:
        return event
    else:
        raise HTTPException(status_code=404, detail='Event not found')


@router.get('/events/{date}/{show_time}/{theatre}')
async def search_event(date: str, show_time: str, theatre: str):
    event = search_event_query(date, show_time, theatre)

    if event:
        return event
    else:
        raise HTTPException(status_code=404, detail='Event not found')


