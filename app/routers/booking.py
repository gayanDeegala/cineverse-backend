from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import json

from app.database.booking import get_booked_seats, update_booked_seats
from app.database.connection import create_mysql_connection
from app.database.event import event_exists

router = APIRouter()


# Define a Pydantic model for the Booking
class Booking(BaseModel):
    seats: List[str]


# API endpoint to get current bookings for an event
@router.get('/bookings/{event_id}')
async def get_bookings(event_id: int):
    booked_seats = get_booked_seats(event_id)

    if booked_seats is not None:
        return {"booked_seats": booked_seats}
    else:
        raise HTTPException(status_code=404, detail='Event not found')


# API endpoint to add bookings for an event
@router.post('/bookings/{event_id}')
async def add_bookings(event_id: int, booking: Booking):
    if not event_exists(event_id):
        raise HTTPException(status_code=404, detail='Event not found')

    existing_booked_seats = get_booked_seats(event_id)

    if existing_booked_seats:
        new_booked_seats = existing_booked_seats + booking.seats
    else:
        new_booked_seats = booking.seats

    update_booked_seats(event_id, new_booked_seats)

    return {'message': 'Bookings added successfully'}
