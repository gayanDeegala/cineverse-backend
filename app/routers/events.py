from fastapi import APIRouter, HTTPException
from app.database.connection import create_mysql_connection
import json

router = APIRouter()


# API endpoint to get all events
@router.get('/events')
async def get_events():
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Query the database to retrieve all events
    query = "SELECT * FROM events"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        events = []
        for row in result:
            event = {
                'id': row[0],
                'date': row[1],
                'show_time': row[2],
                'theatre': row[3],
                'movie_title': row[4],
                'booked_seats': json.loads(row[5])  # Convert the JSON string to a list
            }
            events.append(event)

        return events
    else:
        raise HTTPException(status_code=404, detail='No events found')