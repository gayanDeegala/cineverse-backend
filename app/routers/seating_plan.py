from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
import ast

from app.database.booking import get_booked_seats_query
from app.database.event import event_exists_query, get_event_query
from app.routers.utls.seating_plan import generate_seating_plan

router = APIRouter()


class RowRequest(BaseModel):
    row: str
    headcount: int


class SeatingPlanRequest(BaseModel):
    event_id: int
    rows: List[RowRequest]


@router.post('/seating-plan')
async def get_seating_plan(request: SeatingPlanRequest):
    event_id = request.event_id

    # Check if the event exists
    if not event_exists_query(event_id):
        raise HTTPException(status_code=404, detail='Event not found')

    # Get the event information
    event = get_event_query(event_id)

    # Get the theater seating arrangement
    theater_seating = event['theatre'].get_seating_arrangement()
    if theater_seating is None:
        raise HTTPException(status_code=500, detail='Theater seating arrangement not found')

    # Get the booked seats for the event
    booked_seats_list = ast.literal_eval(get_booked_seats_query(event_id))

    seating_plan = []
    for row_request in request.rows:
        selected_row = row_request.row
        headcount = row_request.headcount

        # Extract the row and seat number from the booked seats
        booked_seats = []
        for seat in booked_seats_list:
            row = seat[0]  # Extract the row from the seat
            seat_number = int(seat[1:])  # Extract the seat number from the seat

            if row == selected_row:  # Only consider seats in the selected row
                if row not in booked_seats:
                    booked_seats.append(seat_number)

        # Generate the seating plan for the row
        row_seating_plan = generate_seating_plan(theater_seating, booked_seats, headcount, selected_row)
        seating_plan.extend(row_seating_plan)

    return {
        'event_id': event_id,
        'seating_plan': seating_plan
    }
