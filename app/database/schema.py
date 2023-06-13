import pymysql

from app.database.connection import create_initial_mysql_connection
from app.database.data.events import events_data, movieTitles
from app.models.emums import Date, ShowTime, Theatre
import json


def create_database(cursor, database_name):
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor.execute(create_database_query)


def create_events_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date VARCHAR(20) NOT NULL,
        show_time ENUM('10:00 AM', '1:00 PM', '4:00 PM', '7:00 PM') NOT NULL,
        theatre ENUM('Theatre 1', 'Theatre 2', 'Theatre 3') NOT NULL,
        movie_title VARCHAR(100) NOT NULL,
        booked_seats TEXT  -- Stores the list of booked seats for the event as a JSON
    )
    """
    cursor.execute(create_table_query)
    
    
def prepopulate_events_table(cursor):
    insert_query = """
    INSERT INTO events (date, show_time, theatre, movie_title, booked_seats)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_query, events_data)


def create_schema():
    connection = create_initial_mysql_connection()
    cursor = connection.cursor()

    # Create the database
    database_name = 'cineverse'
    create_database(cursor, database_name)
    cursor.execute(f"USE {database_name}")

    # Call the function to create the required tables
    create_events_table(cursor)

    # Pre-populate the events table
    prepopulate_events_table(cursor)

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()


# Call the create_schema() function to create the database and tables
# create_schema()
