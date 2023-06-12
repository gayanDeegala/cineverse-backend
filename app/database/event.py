from app.database.connection import create_mysql_connection
from fastapi import HTTPException
import json


def event_exists(event_id: int):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Check if the event exists
    query = f"SELECT id FROM events WHERE id = {event_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None


def get_all_events():
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Query the database to retrieve all events
    query = "SELECT * FROM events"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

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


def get_event_info(date: str, show_time: str, theatre: str):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Query the database to retrieve the event information based on the date, show_time, and theatre
    query = f"SELECT * FROM events WHERE date = '{date}' AND show_time = '{show_time}' AND theatre = '{theatre}'"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        event_id, event_date, event_show_time, event_theatre, event_movie_title, event_booked_seats = result
        event = {
            'id': event_id,
            'date': event_date,
            'show_time': event_show_time,
            'theatre': event_theatre,
            'movie_title': event_movie_title,
            'booked_seats': json.loads(event_booked_seats)  # Convert the JSON string to a list
        }
        return event
    else:
        raise HTTPException(status_code=404, detail='Event not found')