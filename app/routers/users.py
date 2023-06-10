from fastapi import APIRouter
from app.database.connection import create_mysql_connection

router = APIRouter()


@router.get("/users")
def get_users():
    connection = create_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"users": users}