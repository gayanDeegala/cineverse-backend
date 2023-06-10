from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import json

from app.database.connection import create_mysql_connection

router = APIRouter()


# Define a Pydantic model for the Booking
class Booking(BaseModel):
    seats: List[str]


# API endpoint to get current bookings for an event
@router.get('/bookings/{event_id}')
async def get_bookings(event_id: int):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Query the database to retrieve the booked seats for the event
    query = f"SELECT booked_seats FROM events WHERE id = {event_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return result[0]  # Return the booked seats as a JSON string
    else:
        raise HTTPException(status_code=404, detail='Event not found')


# API endpoint to add bookings for an event
@router.post('/bookings/{event_id}')
async def add_bookings(event_id: int, booking: Booking):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Check if the event exists
    query = f"SELECT id FROM events WHERE id = {event_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail='Event not found')

    # Retrieve the existing booked seats for the event from the database
    query = f"SELECT booked_seats FROM events WHERE id = {event_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        existing_booked_seats = json.loads(result[0])  # Convert the JSON string to a list
        new_booked_seats = existing_booked_seats + booking.seats
    else:
        new_booked_seats = booking.seats

    # Update the booked seats in the database
    update_query = f"UPDATE events SET booked_seats = '{json.dumps(new_booked_seats)}' WHERE id = {event_id}"
    cursor.execute(update_query)
    connection.commit()

    return {'message': 'Bookings added successfully'}
