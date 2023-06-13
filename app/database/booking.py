from app.database.connection import create_mysql_connection
import json


def get_booked_seats_query(event_id: int):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Query the database to retrieve the booked seats for the event
    query = f"SELECT booked_seats FROM events WHERE id = {event_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result[0] if result else None


def update_booked_seats_query(event_id: int, seats: list):
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Update the booked seats in the database
    update_query = f"UPDATE events SET booked_seats = '{json.dumps(seats)}' WHERE id = {event_id}"
    cursor.execute(update_query)
    connection.commit()

    cursor.close()
    connection.close()
