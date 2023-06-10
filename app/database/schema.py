import pymysql
from app.database.connection import create_mysql_connection


def create_database(cursor, database_name):
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor.execute(create_database_query)


def create_schema():
    connection = create_mysql_connection()
    cursor = connection.cursor()

    # Create the database
    database_name = 'cineverse'
    create_database(cursor, database_name)
    cursor.execute(f"USE {database_name}")

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()


# Call the create_schema() function to create the database and tables
# create_schema()
